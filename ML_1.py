import numpy as np
import torch
from torch.autograd import Variable
import pandas as pd

#过采样函数
def oversampling(data):
    data0 = data[data[:,0]==0]
    data1 = data[data[:,0]==1]#0、1分开
    size0 = data0.shape[0]
    size1 = data1.shape[0]
    if size0 >= size1:#多的减少的
        index= np.random.choice(size1,size0-size1,replace=False,p=None)#随机采样
        data1 = np.concatenate((data1, data1[index,:]), axis=0)#合并
    else:
        index= np.random.choice(size0,size1-size0,replace=False,p=None)#随机采样
        data0 = np.concatenate((data0, data0[index,:]), axis=0)#合并
    x = np.concatenate((data0[:, 1:31], data1[:, 1:31]), axis=0)#合并
    y = np.concatenate((data0[:, 0:1], data1[:, 0:1]), axis=0)#合并
    return x, y

#对数据进行预处理
def pre_process(dataset):
   data = dataset.iloc[:, 1:32].values
   data[data=='M'] = 1
   data[data=='B'] = 0      #MB分类
   data = data.astype(np.float64)
   x,y = oversampling(data)
   size = x.shape[0]
   index = np.random.permutation(size)       #随机排列
   x = x[index]
   y = y[index]
   mu = np.mean(x, axis=0)
   sigma = np.std(x, axis=0)
   x=(x - mu)/sigma
   split = int(len(y)*0.3)       #0.3
   x_train = x[:split]
   y_train = y[:split]
   x_test = x[split:]
   y_test = y[split:]
   return x_train, y_train, x_test, y_test

#精确度计算
def cal_acc(x, y, y_pred):
    size = x.shape[0]
    y_pred = np.array([0 if y_pred[i] < 0.5 else 1 for i in range(size)])
    acc = np.mean([1 if y[i] == y_pred[i] else 0 for i in range(size)])
    return acc

#模型
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(30, 1) 

    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

#主体
dataset= pd.read_csv('./data.csv')
x_train, y_train, x_test, y_test = pre_process(dataset)#处理
x_train = Variable(torch.Tensor(x_train))
y_train = Variable(torch.Tensor(y_train))
x_test = Variable(torch.Tensor(x_test))
y_test = Variable(torch.Tensor(y_test))
  
model = Model()
criterion = torch.nn.BCELoss(reduction="mean")#损失（二分类交叉熵）
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)#优化器

#进行循环训练
i=50    #隔50个打印
j=1    #计数器
print('每',i,'个epoch一组')

for epoch in range(1000):     #1000个
    optimizer.zero_grad()
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    loss.backward()    #反向传播
    optimizer.step()    #更新优化器
    if epoch % i == 0:    
        print('第',j,'组','损失loss:', loss.data.item(), '精确度accuracy:', cal_acc(x_train, y_train, y_pred))
        j=j+1

y_test_pred = model(x_test)
test_acc = cal_acc(x_test, y_test, y_test_pred)
print('Test总精确度:', test_acc)

for f in model.parameters():
    print('具体数据：')
    print(f.data)
    print(f.grad)



