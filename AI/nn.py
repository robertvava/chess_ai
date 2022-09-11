from torch import nn

loss = nn.CrossEntropyLoss()


class CENN(nn.Module): 
    def __init__(self, loss):
        self.loss = loss
