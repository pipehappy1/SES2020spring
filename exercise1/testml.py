#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:38:02 2020

@author: bxw
"""
import torch
import torch.nn.functional as F
import torch.nn.init as init
import math
import numpy as np
import pandas as pd
from torch.autograd import Variable
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#从本地读取数据
xy = pd.read_csv('./data2.csv').values
x = Variable(torch.from_numpy(xy[:,0:-1]))
y = Variable(torch.from_numpy(xy[:,0]))
#划分训练数据和测试数据
x_train, x_test,y_train,y_test= train_test_split(x.numpy(),y.numpy(), test_size=0.3,random_state=2018)   
ss = StandardScaler()  
#特征归一化
x_train = Variable(torch.tensor(ss.fit_transform(x_train)))
x_test = Variable(torch.tensor(ss.fit_transform(x_test)))
y_train = Variable(torch.tensor(y_train))
y_test = Variable(torch.tensor(y_test))

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.l1 = torch.nn.Linear(31, 33)  
        self.l2 = torch.nn.Linear(33, 33)
        self.l3 = torch.nn.Linear(33, 33)
        self.l4 = torch.nn.Linear(33, 1)
    def forward(self, x):
        x = F.tanh(self.l1(x.float()))
        x = F.tanh(self.l2(x))
        x = F.tanh(self.l3(x))
        x = self.l4(x)
        return x
model = Model()
#model.apply(weights_init)
criterion = torch.nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-1, momentum=0.9)
Loss = []
Acc = []
EPOCHS = 1000
for epoch in range(EPOCHS):
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train.float().view(-1,1))
    preds = torch.tensor(y_pred >= 0)
    corrects = torch.sum(preds.byte() == y_train.view(-1,1).byte())
    acc = corrects.item()/len(x_train)
    if epoch%100 == 0:
        print("corrects:",corrects)
        print("epoch = {0}, loss = {1}, acc = {2}".format(epoch, loss, acc))
        Loss.append(loss)
        Acc.append(acc)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    plt.plot(range(len(Loss)), Loss)
w = list(model.parameters())
w0 = w[0].data.numpy()
w1 = w[1].data.numpy()

import matplotlib.pyplot as plt

print("Final gradient descend:", w)

plt.ylabel('loss')
plt.xlabel('epochs')
plt.show()
plt.plot(range(len(Acc)), Acc)
plt.ylabel('acc')
plt.xlabel('epochs')
plt.show()