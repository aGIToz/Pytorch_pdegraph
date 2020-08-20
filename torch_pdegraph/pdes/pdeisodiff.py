"""
Runs a predefined isotorpic diffusion PDE on graph
Implements the following iterative scheme:

\mathbf{x}^{n+1}_{i} = \frac{\sum_{j \in N(i)} w_{i,j}^{p/2}\|\mathbf{x}^{n}_{j}-\mathbf{x}^{n}_{i}\|_{2}^{p-2}\mathbf{x}^{n}_{j}}{\sum_{j \in N(i)} w_{i,j}^{p/2}\|\mathbf{x}^{n}_{j}-\mathbf{x}^{n}_{i}\|_{2}^{p-2}}

Ref:
(https://hal.archives-ouvertes.fr/hal-00163573/document)
"""
import torch
from torch_geometric.nn import MessagePassing
from tqdm import tqdm

class Numerator(MessagePassing):
    def __init__(self, graph, **kwargs):
        super(Numerator, self).__init__(aggr='add') 
        self.ep = kwargs["epsilon"]
        self.p = kwargs["p_val"]
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self, x):
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)
              
    def message(self, x_i, x_j):
        a = x_j - x_i
        b = torch.norm(a, dim=1)
        b = b * b
        tmp1 =torch.pow((b+self.ep), (self.p-2)/2)
        tmp2 = torch.stack((tmp1,tmp1,tmp1),dim=1)
        tmp = torch.pow(torch.sqrt(self.edge_attr), self.p) * tmp2 * x_j
        return tmp

    def update(self, aggr_out):
        return  aggr_out

class Denominator(MessagePassing):
    def __init__(self,graph, **kwargs):
        super(Denominator, self).__init__(aggr='add') 
        self.ep = kwargs["epsilon"]
        self.p = kwargs["p_val"]
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self, x):
        edge_index = self.edge_index
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_i, x_j):
        a = x_j - x_i
        b = torch.norm(a, dim=1)
        b = b * b
        tmp1 = torch.pow((b+self.ep),(self.p-2)/2)
        tmp2 = torch.stack((tmp1,tmp1,tmp1),dim=1)
        tmp = torch.pow(torch.sqrt(self.edge_attr), self.p) * tmp2 
        return tmp

    def update(self, aggr_out):
        return  aggr_out


class PDE(torch.nn.Module):
    def __init__(self, graph, **kwargs):
        super(PDE, self).__init__()
        self.num = Numerator(graph, **kwargs)
        self.den = Denominator(graph, **kwargs)

    def forward(self,signal,itr):
        for i in tqdm(range(itr)):
            u =  self.num(signal)
            d =  self.den(signal)
            signal = u / d
        return signal
