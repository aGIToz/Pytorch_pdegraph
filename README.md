# Torch_pdegraph
Torch_pdegraph is a proof of concept that how one can solve PDEs (partial difference equations)  on graphs using the Message Passing class of torch_geometric and hence also benefits from the hardware acceleration.

The basic idea is that one can define the operators like, derivatives, gradients, laplacians on graphs and construct a PDE inspired from nature on graphs.
To know more about PDEs on graph.
- Be sure to play with the **jupyter-notebooks in the applications/** folder which presents few of their applications. Download the [data](https://drive.google.com/file/d/1I3IRe1HSoOyh5gBU-cGtLtATWboRMT3-/view?usp=sharing)
- Ref to operator_calculus.md for a brisk intro to calculus on graphs.

## Installation 
First [install](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html) the torch_geometric. Then one can clone this project and install it locally:

```shell
pip install --upgrade pip
pip install .
```

Or do:


```shell
pip install --upgrade pip
pip install torch_pdegraph
```

## Running the notebooks
In the notebooks I am demonstrating few applications of pdes on images and pcd by creating simple knn-graphs on gpu. One will need [faiss](https://github.com/facebookresearch/faiss/blob/master/INSTALL.md) library to create the graphs.

To display the pcds inside the notebook I am using jupyter visualization feature in open3d which uses a jupyter widget, notebooks must be running to for the widget to function.

## To do:
- Add an interpolation application.
- Add a segmentation predefined pde. 
