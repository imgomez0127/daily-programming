import numpy as np
from functools import reduce
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)
        self.linear = nn.Linear(144*20,50)
        self.linear2 = nn.Linear(50,1)
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view(-1,reduce(lambda x,y: x * y,list(x.shape)))
        x = F.relu(self.linear(x))
        x = torch.sigmoid(self.linear2(x))
        return x
    def fit(self,training_data,labels,epochs=7):
        loss_function = torch.nn.BCELoss()
        optimizer = optim.Adam(self.parameters())
        self.train() 
        for _ in range(epochs):
            optimizer.zero_grad()
            value = x(data)
            loss = loss_function(value,label)
            loss.backward()
            print(loss)
            optimizer.step()

if __name__ == "__main__":
    x = Model()
    data = torch.rand((1,1,20,20))
    label = torch.ones((1,1),dtype=torch.float)
    x.fit(data,label,epochs=10) 
    data2 = torch.rand((1,1,20,20))
