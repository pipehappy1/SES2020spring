import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from torch.autograd import Variable

NUM_EPOCH = 512
DTYPE = torch.float
DEVICE = torch.device("cpu")
DATA_PATH = './wdbc.data'

# 读取数据
data = pd.read_csv(DATA_PATH)

data = data.iloc[:, 1:32].values

# 数据预处理
# 将标记转换为1和0，并转换数据类型为fp32
data[data == 'M'] = 1
data[data == 'B'] = 0
data = data.astype(np.float32)
# 划分训练集
x_train, x_test, y_train, y_test = train_test_split(data[:, 1:31],
                                                    data[:, 0],
                                                    test_size=0.3)
# 数据类型和维度转换
x_train = Variable(torch.Tensor(x_train))
x_test = Variable(torch.Tensor(x_test))
y_train = Variable(torch.Tensor(y_train))
y_test = Variable(torch.Tensor(y_test))

y_train = y_train.reshape([-1, 1])
y_test = y_test.reshape([-1, 1])


# 定义torch模型
class torch_model(nn.Module):
    def __init__(self, input, n1, n2, output):
        super(torch_model, self).__init__()
        self.layer1 = nn.Sequential(nn.Linear(input, n1), nn.Sigmoid())
        self.layer2 = nn.Sequential(nn.Linear(n1, n2), nn.Sigmoid())
        self.layer3 = nn.Sequential(nn.Linear(n2, output), nn.Sigmoid())

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x

# 准确率
def Acc(y_pred, y_real):

    y_pred = np.array(y_pred.data)
    y_real = np.array(y_real)
    pred_mean = np.mean(y_pred)
    y_pred[y_pred > pred_mean] = 1.0
    y_pred[y_pred <= pred_mean] = 0.0
    error = np.sum(np.abs(y_pred - y_real))
    return 1 - (error / y_pred.shape[0])


# 模型，优化器，损失函数
model = torch_model(30, 90, 45, 1)
optimizer = optim.Adam(model.parameters(), lr=0.001)
crierion = nn.MSELoss()

E_list = []
L_list = []
A_list = []
# 训练并保存数据
for epoch in range(NUM_EPOCH):
    y_pred = model(x_train)
    loss = crierion(y_pred, y_train)
    accuracy = Acc(y_pred, y_train)
    print("epoch:%d loss:%f accuracy:%f" % (epoch, loss.data.item(), accuracy))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    E_list.append(epoch)
    L_list.append(loss.data.item())
    A_list.append(accuracy)
# 预测数据并评价结果
model.eval()
eval_loss = 0.0
eval_acc = 0.0

y_pred = model(x_test)
loss = crierion(y_pred, y_test)
eval_loss = loss.data.item()

y_test = np.array(y_test)
y_pred = np.array(y_pred.data)
pred_mean = np.mean(y_pred)
y_pred[y_pred > pred_mean] = 1
y_pred[y_pred <= pred_mean] = 0

for i in range(y_pred.shape[0]):
    y_p = y_pred[i]
    y_t = y_test[i]
    if y_p == y_t:
        eval_acc += 1
eval_acc_rare = eval_acc / y_pred.shape[0]
print('accuracy %d in %d' % (int(eval_acc), y_pred.shape[0]))
print('accuracy rate is %f' % (eval_acc / y_pred.shape[0]))

# 训练中损失函数的变化

E = np.array(E_list)
L = np.array(L_list)
A = np.array(A_list)
plt.figure()
plt.plot(E, L)
plt.plot(E, A)
plt.show()
