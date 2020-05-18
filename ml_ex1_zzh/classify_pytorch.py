import numpy as np
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 读取数据
data = pd.read_csv(r"G:\python_work\machine learning\classfication\data.csv")

#良性为0，恶性为1，处理数据集
data.diagnosis = data.diagnosis.map({'M':1, 'B':0})
print(data)
data.drop(['id'], axis = 1, inplace = True)
print(data)

# 进行数据的分割，2到最后列为特征值，1列为目标值
x_train, x_test, y_train, y_test = train_test_split(np.array(data.iloc[:,1:]), np.array(data.iloc[:,0]), test_size=0.3)

# 标准化处理
std = StandardScaler()
x_train = std.fit_transform(x_train) #找到数据的均值方差并标准化
x_test = std.transform(x_test)  #用上一步得到的参数标准化

# 转化为variable类型
x_data = Variable(torch.Tensor(x_train))
y_data = Variable(torch.Tensor(y_train))

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(30, 1) # 30 in and 1 out
        
    def forward(self, x):
        #y_pred = torch.sigmoid(self.linear(x))
        y_pred = self.linear(x).sigmoid()
        return y_pred
    
# Our model    
model = Model()

criterion = torch.nn.BCELoss(reduction="mean")
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(1000):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)
    
    accuracy = 0
    pred=y_pred.detach().numpy()
    for i in range(1,y_train.shape[0]):
        if (pred[i]-0.5)*(y_train[i]-0.5)>=0:
            accuracy += (1 / y_train.shape[0])  # Our model 计算准确率
    loss = criterion(y_pred, y_data)
    print('epoch:',epoch, 'loss:',loss.data.item(),'accuracy:',accuracy)
    
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
