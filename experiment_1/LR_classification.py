# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:28:17 2020

@author: Xiaoyang Zou
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import torch

#读取文件
dataset = pd.read_csv('data.csv')

#将良性B与恶性M编码转为良性0与恶性1编码
diagnosis_coding = {'M':1, 'B':0}
dataset.diagnosis = dataset.diagnosis.map(diagnosis_coding)

#去除无用的id栏以及unnamed32栏
dataset.drop(['id','Unnamed: 32'], axis = 1, inplace = True)

#数据及其标签
data_all = np.array(dataset.iloc[:,1:])
label_all = np.array(dataset['diagnosis'])

#对所有数据进行标准化处理
for i in range(data_all.shape[1]):
    mean = np.mean(data_all[:,i])
    std = np.std(data_all[:,i])
    data_all[:,i] = (data_all[:,i] - mean)/std

#将数据以7:3比例分为训练集与测试集 
x_train, x_test, y_train, y_test = train_test_split(data_all,label_all,train_size = 0.7)

#转换为torch张量
x_train = torch.tensor(x_train).type(torch.FloatTensor)
x_test = torch.tensor(x_test).type(torch.FloatTensor)
y_train = torch.tensor(y_train).type(torch.FloatTensor)
y_test = torch.tensor(y_test).type(torch.FloatTensor)

#定义我们的model
class LogisticRegression(torch.nn.Module):
    def __init__(self):
        super(LogisticRegression, self).__init__()
        self.linear = torch.nn.Linear(30, 1)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        x = self.linear(x)
        x = self.sigmoid(x)
        return x
 
model = LogisticRegression()
if torch.cuda.is_available():
    model.cuda()
 
#定义损失函数为二分类交叉熵，优化器采用SGD
criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3, momentum=0.9)

#将打印结果写入result文件
f = open("result.txt", 'w')
#训练1000个epoch
for epoch in range(1000):
    if torch.cuda.is_available():
        data = torch.autograd.Variable(x_train).cuda()
        label = torch.autograd.Variable(y_train).cuda()
    else:
        data = torch.autograd.Variable(x_train)
        label = torch.autograd.Variable(y_train)
    out = model(data)
    loss = criterion(out, label)
    print_loss = loss.data.item()
    predict = out.ge(0.5).float()   #以0.5为阈值进行分类
    correct = 0
    for i in range(label.size(0)):
        if predict[i] == label[i]:
            correct += 1
    acc = correct / label.size(0)  #计算Accuracy
    optimizer.zero_grad()
    loss.backward() #反向传播
    optimizer.step() #优化器更新
    
    # 每隔20个epoch打印当前的loss和Accuracy
    if (epoch + 1) % 20 == 0:
        print('*'*10,file = f)
        print('epoch {}'.format(epoch+1),file = f) 
        print('loss is {:.4f}'.format(print_loss),file = f)
        print('accuracy is {:.4f}'.format(acc),file = f)      
f.close()