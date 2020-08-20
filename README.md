# Torch_pdegraph
Torch_pdegraph is a proof of concept that how one can solve PDEs (partial difference equations)  on graphs using the Message Passing class of torch_geometric and hence also befits from the hardware acceleration. See the presentation. 

## What is a PDE on a graph?
The basic idea is that one can define the operators like, derivatives, gradients, laplacians on graphs and construct a PDE inspired from nature on graphs.
To know more about PDEs on graph.
- See the publications of [Elmoataz](https://elmoatazbill.users.greyc.fr/pub.html). 
- See also their [applications on pointclouds](https://elmoatazbill.users.greyc.fr/point_cloud/index.html)
- Classical PDEs on images by [Guillermo Sapiro](https://www.youtube.com/watch?v=ZAmig8cw7H8&list=PLEE9b2lRB-R0vii_n3A_3ec9F_Bp_U9Fh&index=2&t=3s)
- Be sure to see the jupyter-notebooks in the **applications/** folder presenting few of their applications. 
- Ref to operator_calculus.md for a brisk intro to calculus on graphs.

## Installation 
First [install](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html) the torch_geometric. Then one can clone this project and install it locally:

```shell
pip install .
```

Or do:

```shell
pip install torch_pdegraph
```

## Running the notebooks
In the notebooks I am demonstrating few applications of pdes on images and pcd by creating simple knn-graphs on gpu. One will need [faiss](https://github.com/facebookresearch/faiss/blob/master/INSTALL.md) library to create the graphs.

To display the pcds inside the notebook I am using jupyter visualization feature in open3d which uses a jupyter widget, notebooks must be running to for the widget to function.

## To do:
- Add an interpolation application.
- Add a segmentation predefined pde. 
