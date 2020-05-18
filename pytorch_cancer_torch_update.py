import numpy as np
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing

#利用sklean自带的cancer数据集
X,T= datasets.load_breast_cancer(return_X_y=True)
#数据预处理，标准化
for i in range(X.shape[1]):
    mean = np.mean(X[:,i])
    std = np.std(X[:,i])
    X[:,i] = (X[:,i] - mean)/std
#划分训练集和测试集，比例为7:3，交叉验证
X_train,X_test,T_train,T_test = train_test_split(X,T,train_size=0.7,test_size=0.3)
x_data = Variable(torch.Tensor(X_train))
y_data = Variable(torch.Tensor(T_train))
x_test = Variable(torch.Tensor(X_test))
t_test = Variable(torch.Tensor(T_test))

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        #self.hidden = torch.nn.Linear(x_data.shape[1])
        self.linear = torch.nn.Linear(x_data.shape[1], 1) # 30 in and 1 out
        
    def forward(self, x):
        #y_pred = torch.sigmoid(self.linear(x))
        y_pred = self.linear(x).sigmoid()
        return y_pred
    
# Our model    
model = Model()

criterion = torch.nn.BCELoss(reduction="mean")
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

f = open("result.txt", 'w')
# Training loop
for epoch in range(1000):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)
    pre=y_pred.ge(0.5).float()
    correct = 0
    for i in range(y_data.size(0)):
        if pre[i] == y_data[i]:
            correct += 1
    acc = correct / y_data.size(0)  #计算Accuracy
    print(epoch,file = f)
    print('accuracy is',acc,file = f)
    
    # 计算损失
    loss = criterion(y_pred, y_data)
    print(' loss is', loss.data.item(),file = f)
    
    # Zero gradients, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

for f in model.parameters():
    print('data is')
    print(f.data)
    print(f.grad)

w = list(model.parameters())
w0 = w[0].data.numpy()
w1 = w[1].data.numpy()

y_pred1 = model(x_test)#预测测试集
pre1=y_pred1.ge(0.5).float()
correct1 = 0
for i in range(t_test.size(0)):
    if pre1[i] == t_test[i]:
        correct1 += 1
acc1 = correct1 / t_test.size(0)  #计算测试集的Accuracy
print('test accuracy is',acc)

import matplotlib.pyplot as plt

print("Final gradient descend:", w)
# plot the data and separating line
plt.scatter(x_data[:,0], x_data[:,1], c=y_data.reshape(len(x_data)), s=100, alpha=0.7)
x_axis = np.linspace(-6, 6, 100)
y_axis = -(w1[0] + x_axis*w0[0][0]) / w0[0][1]
line_up, = plt.plot(x_axis, y_axis,'r--', label='gradient descent')
plt.legend(handles=[line_up])
plt.xlabel('X(1)')
plt.ylabel('X(2)')
plt.show()


