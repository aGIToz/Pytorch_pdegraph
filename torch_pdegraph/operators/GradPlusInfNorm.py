import torch
from torch_geometric.nn import MessagePassing

class OPE(MessagePassing):
    """
    Computes: 
    \|(\nabla_{w}^{+}f(v_{i})\|_{\infty} = \max_{v_{j}\sim v_{i}}\sqrt{w(v_{i},v_{j})}((f(v_j) - f(v_i))^{+} 
    """
    def __init__(self, graph, **kwargs):
        super(OPE, self).__init__(aggr='max') 
        self.edge_index = graph.edge_index
        self.edge_attr = graph.edge_attr

    def forward(self, x):
        return self.propagate(edge_index=self.edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_i, x_j):
        tmp = torch.sqrt(self.edge_attr)  * torch.clamp(x_j-x_i, 0.00)
        return tmp 

    def update(self, aggr_out):
        
        return aggr_out
