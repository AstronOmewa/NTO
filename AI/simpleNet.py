import torch
import torch.nn as nn

class simpleNN(nn.Module):
    def __init__(self):
        super(simpleNN, self).__init__()
        self.fc1 = nn.Linear(728,128)
        self.fc2 = nn.Linear(128,10)

    def forward(self, x):
        x = torch.relu(torch.fc1(x))
        return self.fc2
    
