"""
Runs a predefined anisotropic diffusion PDE on graph:
Implements the following iterative scheme:

\mathbf{x}^{n+1}_{i} = \frac{\lambda \mathbf{x}^{0}_{i} + \sum_{j \in N(i)} w_{i,j}^{p/2}|\mathbf{x}^{n}_{j}-\mathbf{x}^{n}_{i}|^{p-2}\mathbf{x}^{n}_{j}}{\lambda+ \sum_{j \in N(i)} w_{i,j}^{p/2}|\mathbf{x}^{n}_{j}-\mathbf{x}^{n}_{i}|^{p-2}}

Ref:
https://hal.archives-ouvertes.fr/hal-00163573/document
"""

import torch
from torch_geometric.nn import MessagePassing
from tqdm import tqdm

class Numerator(MessagePassing):
    def __init__(self, graph, **kwargs):
        super(Numerator, self).__init__(aggr='add') #  "add" aggregation.
        self.ep = kwargs["epsilon"]
        self.lamb = kwargs["lamb"]
        self.p = kwargs["p_val"]
        self.x0 = kwargs["x0"]
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self, x):
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_i, x_j):
        tmp = torch.pow(torch.sqrt(self.edge_attr), self.p) * torch.pow(torch.abs((x_j - x_i) + self.ep), self.p-2) * x_j 
        return tmp

    def update(self, aggr_out):
        return self.x0 * self.lamb  + aggr_out

class Denominator(MessagePassing):
    def __init__(self, graph, **kwargs):
        super(Denominator, self).__init__(aggr='add') #  "add" aggregation.
        self.ep = kwargs["epsilon"]
        self.lamb = kwargs["lamb"]
        self.p = kwargs["p_val"]
        self.x0 = kwargs["x0"]
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self, x):
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_i, x_j):
        tmp =  torch.pow(torch.sqrt(self.edge_attr), self.p) * torch.pow(torch.abs((x_j - x_i) + self.ep),self.p-2)
        return tmp

    def update(self, aggr_out):
        return self.lamb + aggr_out


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
