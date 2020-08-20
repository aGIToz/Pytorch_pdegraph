A swift introduction to maths on weighted finite graphs. 

## Basic concepts \& notations
- A graph <img src="svgs/85cc40412fab59dd8312996836032832.svg?invert_in_darkmode" align=middle width=93.85002pt height=24.65759999999998pt/> is composed of an ensemble of nodes (vertices) <img src="svgs/76105ebc974ce8a02de91bcaf0d6d25f.svg?invert_in_darkmode" align=middle width=11.424765000000004pt height=22.46574pt/>, an ensemble of edges <img src="svgs/7114e8b70a29f3808a4b0ac1fc360fba.svg?invert_in_darkmode" align=middle width=10.146180000000003pt height=22.46574pt/> and  weights <img src="svgs/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode" align=middle width=12.210990000000004pt height=14.155350000000013pt/>.
- <img src="svgs/5af5dfedd85fdeaae16799851aa32dff.svg?invert_in_darkmode" align=middle width=14.628075000000004pt height=14.61206999999998pt/> represents the feature vector (signal) on the node <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.663295000000005pt height=21.683310000000006pt/> of <img src="svgs/68a463cbf8842017bbbab8ca879333c7.svg?invert_in_darkmode" align=middle width=10.753545000000003pt height=22.46574pt/>.
- <img src="svgs/9982a9d682d08696452d15a2576d80da.svg?invert_in_darkmode" align=middle width=26.428050000000002pt height=14.155350000000013pt/> represents the scalar weight on the edge from the node <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.663295000000005pt height=21.683310000000006pt/> to <img src="svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.710483000000004pt height=21.683310000000006pt/>.
- <img src="svgs/aecc6bc1eedb9ff765636932647c2371.svg?invert_in_darkmode" align=middle width=61.25031pt height=24.65759999999998pt/> means  node <img src="svgs/36b5afebdba34564d884d347484ac0c7.svg?invert_in_darkmode" align=middle width=7.710483000000004pt height=21.683310000000006pt/> in the neighborhood of node <img src="svgs/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode" align=middle width=5.663295000000005pt height=21.683310000000006pt/>, which implies <img src="svgs/c9647823ee5e8d05324d75cee87fecd2.svg?invert_in_darkmode" align=middle width=57.386835000000005pt height=22.831379999999992pt/> 
- It is assumed that <img src="svgs/c46b0a73b23393bd36737dbabb050895.svg?invert_in_darkmode" align=middle width=68.31957pt height=24.65759999999998pt/> where <img src="svgs/d3584db9cb169974e404d7a462a8eb24.svg?invert_in_darkmode" align=middle width=38.25145500000001pt height=24.65759999999998pt/> represents the Hilbert space of functions with values in <img src="svgs/1a2503597aeadb3519e1a57389e64b82.svg?invert_in_darkmode" align=middle width=20.774655000000003pt height=27.91271999999999pt/> over the vertices <img src="svgs/76105ebc974ce8a02de91bcaf0d6d25f.svg?invert_in_darkmode" align=middle width=11.424765000000004pt height=22.46574pt/> of <img src="svgs/68a463cbf8842017bbbab8ca879333c7.svg?invert_in_darkmode" align=middle width=10.753545000000003pt height=22.46574pt/>. Each function <img src="svgs/88b0225dd0f0d709c42ef25c85a7f560.svg?invert_in_darkmode" align=middle width=81.44565pt height=27.91271999999999pt/> associates a vector value <img src="svgs/5af5dfedd85fdeaae16799851aa32dff.svg?invert_in_darkmode" align=middle width=14.628075000000004pt height=14.61206999999998pt/> at each <img src="svgs/5400c9e4aa85530857f423dc3663e46a.svg?invert_in_darkmode" align=middle width=37.17912pt height=22.46574pt/>. By definition a Hilbert spaces possesses things like inner products, norms and allows techniques of calculus to be used. 
- Assuming that node feature <img src="svgs/0708a7aa93cb00a678b8378bf3cb747d.svg?invert_in_darkmode" align=middle width=16.081725000000002pt height=14.61206999999998pt/> has <img src="svgs/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode" align=middle width=8.556075000000003pt height=22.831379999999992pt/> dimensions, *i.e.* a vector with <img src="svgs/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode" align=middle width=8.556075000000003pt height=22.831379999999992pt/> scalar components, each of the following the operators applies to the individual scalar components rather than the whole vector.
- Hence <img src="svgs/2ed95826b1b60194c780b949ffdfbf7f.svg?invert_in_darkmode" align=middle width=38.967885pt height=22.46574pt/> doesn't represent the Jacobian of <img src="svgs/5af5dfedd85fdeaae16799851aa32dff.svg?invert_in_darkmode" align=middle width=14.628075000000004pt height=14.61206999999998pt/> but rather gradient on each scalar component of <img src="svgs/5af5dfedd85fdeaae16799851aa32dff.svg?invert_in_darkmode" align=middle width=14.628075000000004pt height=14.61206999999998pt/>
- The following calculus applies to both directed or symmetric finite graphs

## Operator calculus
-  Weighted difference (or weighted graph derivative) operator:
<p align="center"><img src="svgs/00b3f3e3d6bc50b4b3f77a233b827fd4.svg?invert_in_darkmode" align=middle width=145.501125pt height=26.15679pt/></p>

- The gradient is given by:
<p align="center"><img src="svgs/99a6fd0b48a17bb3a4de8a55c383d353.svg?invert_in_darkmode" align=middle width=131.153055pt height=20.951535pt/></p>

- The <img src="svgs/1896f4b1cd320a0c19bfdbfc9befc483.svg?invert_in_darkmode" align=middle width=11.681340000000004pt height=22.831379999999992pt/> norm of gradient is given by:
<p align="center"><img src="svgs/06f82d5a668a63fa5e9163b093545163.svg?invert_in_darkmode" align=middle width=263.26245pt height=64.828995pt/></p>

```python
# Example
from torch_pdegraph.utilities import Graph
graph = Graph(edge_index, edge_attr)

from torch_pdegraph.operators import GradNorm
ope = GradNorm.OPE(graph,**(p_val=p))
ope(node_features)
```


- The <img src="svgs/5c5b04bc8c9e7b8f84c87d8f7ec4dadd.svg?invert_in_darkmode" align=middle width=18.010080000000002pt height=22.831379999999992pt/> norm of gradient is given by:
<p align="center"><img src="svgs/bd1e4a630163d73f5648042efe3c5621.svg?invert_in_darkmode" align=middle width=244.80884999999998pt height=33.583769999999994pt/></p>

```python
from torch_pdegraph.operators import GradInfNorm
```
- The partial directional differences are:

<p align="center"><img src="svgs/5a20517a9641a91906f46a12c2451ee6.svg?invert_in_darkmode" align=middle width=112.26682499999998pt height=48.524849999999994pt/></p>

&emsp;&emsp;  where:

<p align="center"><img src="svgs/63fde7548c01f603ec8af2f060098505.svg?invert_in_darkmode" align=middle width=135.42045pt height=18.020145pt/></p>

<p align="center"><img src="svgs/8c6e794af5be87c66c06f17bdc0f038e.svg?invert_in_darkmode" align=middle width=148.38845999999998pt height=18.020145pt/></p>

- The directional gradients are given by:
<p align="center"><img src="svgs/9beff79664a5abba8bc57d5b348f8de9.svg?invert_in_darkmode" align=middle width=138.60841499999998pt height=27.83319pt/></p>

<p align="center"><img src="svgs/12e2b0ee01fa6e8ce4cadc0d84398c76.svg?invert_in_darkmode" align=middle width=138.97356pt height=27.83319pt/></p>

- The norms of those gradients:

<p align="center"><img src="svgs/df29c6a2b9259375a0f50b89f4591ee2.svg?invert_in_darkmode" align=middle width=290.88674999999995pt height=64.828995pt/></p>

<p align="center"><img src="svgs/dd35b39acc7fd6fc04ed20cfd0408dfd.svg?invert_in_darkmode" align=middle width=291.2514pt height=64.828995pt/></p>

```python
from torch_pdegraph.operators import GradPlusNorm
from torch_pdegraph.operators import GradMinusNorm
```

- The infinity norm of those gradients:

<p align="center"><img src="svgs/3648a4c7313b17c42cbc36107a56c74a.svg?invert_in_darkmode" align=middle width=259.6473pt height=33.583769999999994pt/></p>

<p align="center"><img src="svgs/1b442be9b166934b13f739e0affa7237.svg?invert_in_darkmode" align=middle width=260.01194999999996pt height=33.583769999999994pt/></p>

```python
from torch_pdegraph.operators import GradPlusInfNorm
from torch_pdegraph.operators import GradMinusInfNorm
```

- The relationship between the non-directional and directional norm:

<p align="center"><img src="svgs/230557e88e4460295126c56cacd82297.svg?invert_in_darkmode" align=middle width=233.39414999999997pt height=18.613815pt/></p>

<p align="center"><img src="svgs/2a0857f764f8757041a873913bad17f8.svg?invert_in_darkmode" align=middle width=283.79505pt height=18.020145pt/></p>

- The isotopic p-laplacian is give by:

<p align="center"><img src="svgs/184e562a2170cf079feca95a605d5b21.svg?invert_in_darkmode" align=middle width=415.73729999999995pt height=40.548089999999995pt/></p>

```python
from torch_pdegraph.operators import LapIso
```
- The anisotropic p-laplacian is given by:

<p align="center"><img src="svgs/ca8510b69f8abbf157d6d162f614176e.svg?invert_in_darkmode" align=middle width=306.10305pt height=41.762655pt/></p>

```python
from torch_pdegraph.operators import LapAnIso
```

&emsp; &emsp; Notice that for p=2
<p align="center"><img src="svgs/89a2a18fde66a4e812973c9ea0e2a160.svg?invert_in_darkmode" align=middle width=91.13659499999999pt height=20.702714999999998pt/></p>

- The infinity laplacian is given by:
<p align="center"><img src="svgs/790a8b38322a496f64b67dbdd543a96d.svg?invert_in_darkmode" align=middle width=273.92639999999994pt height=32.9901pt/></p>

- The mean curvature is given by:

<p align="center"><img src="svgs/1ffe86dc8b7864b56c0d33fcb2c87ef0.svg?invert_in_darkmode" align=middle width=266.32649999999995pt height=58.893449999999994pt/></p>

```python
from torch_pdegraph.operators import MeanCurv
```

- Add more ...
