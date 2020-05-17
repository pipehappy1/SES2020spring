# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:18:01 2020

@author: gylao
"""

import numpy as np
import torch
from torch.autograd import Variable
import pandas as pd

def undersampling(data):
    data0 = data[data[:,0]==0]
    data1 = data[data[:,0]==1]
    size0 = data0.shape[0]
    size1 = data1.shape[0]
    if size0 >= size1:
        index= np.random.choice(size0,size1,replace=False,p=None)
        data0 = data0[index,:]
    else:
        index= np.random.choice(size1,size0,replace=False,p=None)
        data1 = data1[index,:]
    x = np.concatenate((data0[:, 1:31], data1[:, 1:31]), axis=0)
    y = np.concatenate((data0[:, 0:1], data1[:, 0:1]), axis=0)
    return x, y

def oversampling(data):
    data0 = data[data[:,0]==0]
    data1 = data[data[:,0]==1]
    size0 = data0.shape[0]
    size1 = data1.shape[0]
    if size0 >= size1:
        index= np.random.choice(size1,size0-size1,replace=False,p=None)
        data1 = np.concatenate((data1, data1[index,:]), axis=0)
    else:
        index= np.random.choice(size0,size1-size0,replace=False,p=None)
        data0 = np.concatenate((data0, data0[index,:]), axis=0)
    x = np.concatenate((data0[:, 1:31], data1[:, 1:31]), axis=0)
    y = np.concatenate((data0[:, 0:1], data1[:, 0:1]), axis=0)
    return x, y

def pre_process(dataset):
    data = dataset.iloc[:, 1:32].values
    data[data=='M'] = 1
    data[data=='B'] = 0
    data = data.astype(np.float64)

    #x, y = undersampling(data)
    x, y = oversampling(data)  
    size = x.shape[0]
    index = np.random.permutation(size)
    x = x[index]
    y = y[index]

    mu = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    x =  (x - mu) / sigma

    split = int(len(y)*0.7)
    x_train = x[:split]
    y_train = y[:split]
    x_test = x[split:]
    y_test = y[split:]  
    return x_train, y_train, x_test, y_test

def cal_acc(x, y, y_pred):
    size = x.shape[0]
    y_pred = np.array([0 if y_pred[i] < 0.5 else 1 for i in range(size)])
    acc = np.mean([1 if y[i] == y_pred[i] else 0 for i in range(size)])
    return acc

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(30, 1) 
        
    def forward(self, x):
        y_pred = torch.sigmoid(self.linear(x))
        #y_pred = self.linear(x).sigmoid()
        return y_pred


dataset = pd.read_csv('./data/data.csv')
x_train, y_train, x_test, y_test = pre_process(dataset)
x_train = Variable(torch.Tensor(x_train))
y_train = Variable(torch.Tensor(y_train))
x_test = Variable(torch.Tensor(x_test))
y_test = Variable(torch.Tensor(y_test))
    
# Our model    
model = Model()
criterion = torch.nn.BCELoss(reduction="mean")
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(1000):
    optimizer.zero_grad()
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print('Loss is : ', loss.data.item(), ' Acc is : ', cal_acc(x_train, y_train, y_pred))

y_test_pred = model(x_test)
test_acc = cal_acc(x_test, y_test, y_test_pred)
print('Test Acc is:', test_acc)

for f in model.parameters():
    print('data is')
    print(f.data)
    print(f.grad)

