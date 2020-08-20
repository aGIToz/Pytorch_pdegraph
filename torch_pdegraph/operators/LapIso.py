import torch
from torch_geometric.nn import MessagePassing
from ..operators import GradNorm

class OPE(MessagePassing): 
    """
    Computes:
    \sum_{j\in N(i)} w_{i,j}\ (\|\nabla_{w}\mathbf{x}_{i}\|_{2}^{p-2} + \|\nabla_{w}\mathbf{x}_{j}\|_{2}^{p-2})\  (\mathbf{x}_{j} - \mathbf{x}_{i})
    """
    def __init__(self, graph, **kwargs):
        super(OPE, self).__init__(aggr='add') 
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr
        self.ope = GradNorm.OPE(graph, **kwargs)
        self.p = kwargs["p_val"]
        
    def forward(self, signal):
        new_sig = self.ope(signal)
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x, gradSig = new_sig) 

    def message(self, x_i, x_j, gradSig_i, gradSig_j):
        tmp = 0.5 * self.edge_attr * (torch.pow(gradSig_i, self.p-2) + torch.pow(gradSig_i, self.p-2)) * (x_j - x_i)
        return tmp
