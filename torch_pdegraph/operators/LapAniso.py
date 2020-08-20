import torch
from torch_geometric.nn import MessagePassing

class OPE(MessagePassing): 
    """
    Computes:
    \sum_{j\in N(i)} w_{i,j}^{\frac{p}{2}}\  |\mathbf{x}_{j} - \mathbf{x}_{i} |^{p-2} \  (\mathbf{x}_{j} - \mathbf{x}_{i})

    """
    def __init__(self, graph, **kwargs):
        super(OPE, self).__init__(aggr='add') 
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr
        self.p = kwargs["p_val"]
        
    def forward(self, signal):
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_i, x_j):
        tmp = torch.pow(torch.sqrt(self.edge_attr), self.p) * torch.pow(torch.abs(x_j - x_i), self.p - 2) * (x_j - x_i)
        return tmp
