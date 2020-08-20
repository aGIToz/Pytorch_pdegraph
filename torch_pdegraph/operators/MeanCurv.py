import torch
from torch_geometric.nn import MessagePassing

class Numerator(MessagePassing):
    def __init__(self, graph, **kwargs):
        super(Numerator, self).__init__(aggr='add') 
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self, x):
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_i, x_j):
        return torch.sqrt(self.edge_attr)  * torch.sign(x_j-x_i) 

class Denominator(MessagePassing):
    def __init__(self, graph, **kwargs):
        super(Denominator, self).__init__(aggr='add') 
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self):
        return self.propagate(edge_index = self.edge_index)

    def message(self):
        return torch.sqrt(self.edge_attr) 

class OPE(torch.nn.Module):
    """
    Computes: 
    \kappa_{w}(u,f) = \frac{\sum_{v\sim u}\sqrt{w(u,v)}sign(f(v)-f(u))}{\sum_{v\sim u}\sqrt{w(u,v)}}
    """
    def __init__(self, graph, **kwargs):
        super(OPE, self).__init__() 
        self.num = Numerator(graph, **kwargs)
        self.den = Denominator(graph, **kwargs)

    def forward(self, signal):
        signal = self.num(signal)/self.den()
        return signal
