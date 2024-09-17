import numpy as np
import torch
import torch.nn.functional as F
from torch.autograd import Variable

X = np.loadtxt(open("C:/Users/ThinkPad/PycharmProjects/opticalsimulator/untitled/data_normalized.csv", "rb"), delimiter=",", skiprows=0)
D = X.shape[1]
N = X.shape[0]


# labels: first N/2 are 0, last N/2 are 1
T = np.array([0] * (N // 2) + [1] * (N // 2 + 1)).reshape(N, 1)

x_data = Variable(torch.Tensor(X))
y_data = Variable(torch.Tensor(T))


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.hidden = torch.nn.Linear(D,10) # hidden layer
        self.linear = torch.nn.Linear(10, 1)  # D in and 1 out

    def forward(self, x):
        # y_pred = torch.sigmoid(self.linear(x))
        x = self.hidden(x).sigmoid()
        y_pred = self.linear(x).sigmoid()
        return y_pred


# Our model
model = Model()

criterion = torch.nn.BCELoss(reduction="mean")
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# Training loop
for epoch in range(1000):
    # Forward pass: Compute predicted y by passing x to the model
    y_pred = model(x_data)

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
print(w)