"""
Runs a predefined morphological dilation on graphs.

Solves the following problem:
    \left\{\begin{matrix}
      \frac{\partial f(u, t)}{\partial t}
        = \left\|\nabla_{\omega}^{+}(f)(u) \right\|_{\infty}
    \\
      f(u, 0) = f^{0}(u)
    \end{matrix}\right.

Implements the following iterative scheme:
    f^{n+1}(u) = f^{n}(u) + \left\|\nabla_{\omega}^{+}(f)(u) \right\|_{\infty}

Ref:
  V.-T. Ta, A. Elmoataz et O. Lézoray :<br>
  Nonlocal pdes-based morphology on weighted<br>
  graphs for image and data processing. IEEE<br>
  Trans. Image Process., 20(6):1504–1516, 2011.
"""

import torch
from ..operators import GradPlusInfNorm
from tqdm import tqdm

class PDE(torch.nn.Module):
    def __init__(self, graph, **kwargs):
        super(PDE, self).__init__()
        self.ope = GradPlusInfNorm.OPE(graph, **kwargs)

    def forward(self,signal,itr):
        for i in tqdm(range(itr)):
            signal = signal + self.ope(signal)
        return signal
