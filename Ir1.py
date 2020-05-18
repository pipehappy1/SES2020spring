import numpy as np
import torch
import torch.nn.functional as F
import csv
import pandas as pd
from torch.autograd import Variable


j = 0
j2= 0
right=0;
X=np.zeros((469,30))*2
test=np.zeros((100,30))*2
df = pd.read_csv('data.csv',header=None)
list1=df.values.tolist()

#训练集
for i in list1[1:470]: 
  X[j]=i[2:32]
  j=j+1
for i in range(X.shape[1]):
  mean = np.mean(X[:,i])
  std=np.std(X[:,i])
  X[:,i]=(X[:,i]-mean)/std
print(X)

#测试集
for i in list1[471:570]:
  test[j2]=i[2:32]
  j2=j2+1
for i in range(test.shape[1]):
  mean = np.mean(test[:,i])
  std=np.std(test[:,i])
  test[:,i]=(test[:,i]-mean)/std
print(test)

# labels: first N/2 are 0, last N/2 are 1
T = np.array([0]*(189) + [1]*(280)).reshape(469,1)

x_data = Variable(torch.Tensor(X))
y_data = Variable(torch.Tensor(T))
print(x_data)
print(y_data)
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(30, 1) # 2 in and 1 out
        
    def forward(self, x):
        #y_pred = torch.sigmoid(self.linear(x))
        y_pred = self.linear(x).sigmoid()
        return y_pred
    
# Our model    
model = Model()

criterion = torch.nn.BCELoss(reduction="mean")
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)
    #print(y_pred)
    # Compute and print loss
    loss = criterion(y_pred, y_data)
    print(epoch, loss.data.item())
    
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
import matplotlib.pyplot as plt

print("Final gradient descend:", w)
j3 = 0
for i in range(10000):
  if (j3<=23)and (torch.matmul(w[0],Variable(torch.Tensor(test[j3])))<0.5): right=right+1
  elif(j3>23)and (torch.matmul(w[0],Variable(torch.Tensor(test[j3])))>0.5): right=right+1
  j3=j3+1
print(right/100)
#plot the data and separating line
plt.scatter(X[:,0], X[:,1], c=T.reshape(len(x_data)), s=469, alpha=0.5)
x_axis = np.linspace(-6, 6, 469)
y_axis = -(w1[0] + x_axis*w0[0][0]) / w0[0][1]
line_up, = plt.plot(x_axis, y_axis,'r--', label='gradient descent')
plt.legend(handles=[line_up])
plt.xlabel('X(1)')
plt.ylabel('X(2)')
plt.show()