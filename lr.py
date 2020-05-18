import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch import nn
from torch.autograd import Variable

# 数据导入和预处理
data = pd.read_csv('data.csv')
data.head()
X = data.drop(columns=['id','diagnosis'])
y = data['diagnosis']
y = y.map({'M':0, 'B':1})
X = np.array(X)
y = np.array(y)
x_data = Variable(torch.Tensor(X))
y_data = Variable(torch.Tensor(y))
X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3) # 70%用来训练，30%用来测试


# 搭建一个三层的网络
class Model(nn.Module):

    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(Model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(in_dim, n_hidden_1), nn.Sigmoid())
        self.layer2 = nn.Sequential(nn.Linear(n_hidden_1, n_hidden_2), nn.Sigmoid())
        self.layer3 = nn.Sequential(nn.Linear(n_hidden_2, out_dim),nn.Sigmoid())

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x


# Our model
model = Model(30, 300, 30, 1)  # 输入数据是30维，输出是1维的
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
criterion = torch.nn.BCELoss(reduction="mean")

# 训练模型
for epoch in range(1000):
    y_pred = model(X_train)
    loss = criterion(y_pred, y_train)
    print("epoch:%d loss:%f"%(epoch, loss.data.item()))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

for f in model.parameters():
    print('data is')
    print(f.data)
    print(f.grad)

#模型测试
model.eval()
eval_loss = 0
eval_acc = 0
for data in X_test:
    y_pred = model(X_test)

    # Compute and print loss
    loss = criterion(y_pred, y_test)
    eval_loss += loss.data.item()
for i in range(len(y_pred)):
    if y_pred[i]>0.5:
        y_pred[i] = 1
    else:
        y_pred[i] = 0
    num_correct = (y_pred[i] == y_test[i])
    eval_acc += int(num_correct)
print('Test Loss: {:.6f}, Acc: {:.6f}'.format(
    eval_loss / (len(X_test)),
    eval_acc / (len(X_test))
))




