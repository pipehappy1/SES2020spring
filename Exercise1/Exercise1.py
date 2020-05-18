import matplotlib.pyplot as plt
import numpy as np
import xlrd
import xlsxwriter
import math
import random

ExcelFile=xlrd.open_workbook(r'C:\Users\Aurora\Desktop\data.xlsx')
data=ExcelFile.sheet_by_index(0)


size=569
X = [[0 for i in range(30)] for j in range(size)]
W = [random.uniform(-0.3,0.3) for i in range(31)]  ##随机生成权值W
Y = [0 for i in range(size)]
dL = [0 for i in range(size)]  ##dL/dz
alpha=0.001


for i in range (1,round(0.7*size)):  ###初始化输入X
    for j in range(2,32):
       X[i-1][j-2]=data.cell_value(i,j)

def sigmoid(x):
    return 1/(1+math.exp(-x))

n=80  ##训练次数n
while(n):
  sumdL=0

  for i in range (0,round(0.7*size)-1):  ##用70%训练模型
      z=0                           ##z暂时储存每一次的wx，最后相加得到总的W*X
      y = data.cell_value(i + 1, 1)

      for j in range(0,30):
          z=z+W[j]*X[i][j]+W[30]  ##z=wx+b, b为W[30]

      Y[i]=sigmoid(z)
      try:
          dL[i]=-y/(1+math.exp(z)) + (1-y)/(1+math.exp(-z))
      except OverflowError:
          dL[i]=-y/(1+math.exp(z/10)) + (1-y)/(1+math.exp(-z/10)) ##防止计算exp发生溢出

      sumdL=sumdL+dL[i]   ##dL求和

  for i in range(0,30):
      W[i] = W[i] - alpha/30*sumdL

  n=n-1

correctNum=0
for k in range (round(0.7*size),size-1):  ##用另外30%测试模型
    z=0                           ##z暂时储存每一次的wx，最后相加得到总的W*X
    y = data.cell_value(k + 1, 1)
    for j in range(0,30):
        z=z+W[j]*X[k][j]+W[30]  ##z=wx+b, b为W[30]
    Y[k]=sigmoid(z)

    if ((y-Y[k])*(y-Y[k])<0.25):  ##如果输出Y在0.5以下，认为是0类，在0.5以上，为1类

        correctNum+=1

print('测试样本正确率: ',correctNum/(0.3*size))



