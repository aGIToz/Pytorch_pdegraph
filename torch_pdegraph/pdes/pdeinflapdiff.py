"""
Runs a predefined infinitylaplacian diffusion PDE on graph:

Solves the following problem:
  \left\{\begin{matrix}
      \frac{\partial f(u, t)}{\partial t}
        = \Delta_{\omega, \infty}(f)(u)
    \\
      f(u, 0) = f^{0}(u)
    \end{matrix}\right.

Implements the following iterative scheme:
    f^{n+1}(u) = f^{n}(u) + 0.5 * ( \left\|\nabla_{\omega}^{+}(f)(u) \right\|_{\infty} - \left\|\nabla_{\omega}^{-}(f)(u) \right\|_{\infty})
    Or
    f^{n+1}(u) = f^{n}(u) + 0.5 * (nld(signal) - nle(signal)

Ref:
Abderrahim Elmoataz, Xavier Desquesnes, Zakaria Lakhdari,
and Olivier Lezoray. On the infinity laplacian equation on
graph with applications to image and manifolds processing.
In International Conference on Approximation Methods and
Numerical Modelling in Environment and Natural Resources,
pages 7–pages, 2011.  
"""
import torch
from ..operators import GradMinusInfNorm
from ..operators import GradPlusInfNorm
from tqdm import tqdm

class PDE(torch.nn.Module):
    def __init__(self, graph, **kwargs):
        super(PDE, self).__init__():
        self.ope_m = GradMinusInfNorm.OPE(graph, **kwargs)
        self.ope_p = GradPlusInfNorm.OPE(graph, **kwargs)

    def forward(self,signal,itr):
        for i in tqdm(range(itr)):
            signal = signal +  0.5 * (self.ope_p(signal) - self.ope_m(signal))
        return signal
