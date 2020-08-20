import torch
from torch_geometric.nn import MessagePassing

class OPE(MessagePassing):
    """
    Computes:
    \|(\nabla^{+}_{w}f(v_{i})\|_{p} = \left [ \sum_{v_{j}\sim v_{i}} w(v_{i}v_{j})^{\frac{p}{2}}((f(v_j) - f(v_i))^{+})^{p}  \right]^{\frac{1}{p}}
    """
    def __init__(self, graph, **kwargs):
        super(OPE, self).__init__(aggr='add') 
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr
        self.p = kwargs["p_val"]

    def forward(self, x):
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_i, x_j):
        return torch.pow(torch.sqrt(self.edge_attr)  * torch.clamp(x_j-x_i, 0), self.p) 

    def update(self, aggr_out):
        return torch.pow(aggr_out, 1/self.p)
