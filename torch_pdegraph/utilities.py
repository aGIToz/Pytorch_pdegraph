"""
Azad Amitoz, 2020-08-17
This module allows some basic operations on images and poinclouds. 
Helps creating initial generalized-distances and level-sets.
"""

import numpy as np
from matplotlib import pyplot as plt
import open3d as o3d

def toFmat(img):
    """
    Converts to your image to feature matrix of size (N by c), N is the 
    number of pixels and c is number of channels

    param img: A gray-scale or multi-channel image.
    return fmat: A (N,c) size feature matrix.
    """
    try:
        l, w, c = img.shape
        fmat = np.ones((l*w,c)) 
        for i in range(c): fmat[:,i] = np.reshape(img[:,:,i],(l*w,))
    except ValueError:
        try:
            l, w = img.shape
            fmat = np.ones((l*w,1)) 
            fmat = np.reshape(img,(l*w,1))
        except ValueError:
            print("Image should be at least a 2D array.")
    return fmat

def toPmat(shape):
    """
    Returns the meshgrid of shape (N, M) as position vector of shape (N*M,2)

    param shape: A tuple, shape of an image say of size  (N,M)
    return pmat: postion vector of shape of size (N*M, 2) 
    """
    x = np.arange(0,shape[1],1)
    y = np.arange(shape[0],0,-1)
    meshx, meshy = np.meshgrid(x,y)
    x = np.reshape(meshx,(shape[0]*shape[1],1)) 
    y = np.reshape(meshy,(shape[0]*shape[1],1)) 
    pmat = np.concatenate((x,y),axis=1) / max(shape[0],shape[1])
    return pmat

def getWgStats(wg):
    return f"The max is {np.max(wg)}; The min is {np.min(wg)}; The std is {np.std(wg)};  The median is {np.median(wg)}; The mean is {np.mean(wg)}"

def addNoise(mu, img):
    """
    Adds some white guassian noise

    param mu: What percentage of noise to be added relative the max signal in image
    param img:  Input image
    return signal: The noisy image
    """
    mu = (mu * np.max(img))/100 # TAKE VALUE ACC TO THE MAX VALUE IN IMAGE
    noise = np.random.normal(0, mu, img.shape)
    signal = noise + img
    return signal

def toImg(fmat, shape):
    """
    Converts the (N,c) feature matrix back to original image

    param fmat: The feature matrix of size (N,c)
    param shape: The tuple (N1, N2) assuming N1*N2 = N
    return img: The (N1,N2) shaped image 
    """
    img = np.zeros(shape)
    try:
        l, w, c = img.shape
        for i in range(c): img[:,:,i] = np.reshape(fmat[0:,i],(l,w))
    except ValueError:
        try:
            l, w = img.shape
            img = np.reshape(fmat,(l,w))
        except ValueError:
            print("Image should be at least a 2D array.")
    return img

def getPSNR(imgr, imgt):    
    """
    To get the PSNR

    param imgr: Reference image
    param imgt: Target image
    """
    mse = np.mean( (imgr - imgt) ** 2 )
    if mse == 0: return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def imgPatches(img, patch_shape=(3, 3)):
    """
    Generates the image patches.

    param img: The input image containing N-pixels.
    param patch_shape: The shape of the patches required, say (m,n)
    return patches: The patches feature vector in shape (N, m*n)
    """
    try:
        h, w, d = img.shape
    except ValueError:
        try:
            h, w = img.shape
            d = 0
        except ValueError:
            print("Image should be at least a 2D array.")
    try:
        r, c = patch_shape
    except ValueError:
        r = patch_shape[0]
        c = r
    pad_width = [(int((r - 0.5) / 2.), int((r + 0.5) / 2.)),
                 (int((c - 0.5) / 2.), int((c + 0.5) / 2.))]
    if d == 0:
        window_shape = (r, c)
        d = 1  # For the reshape in the return call
    else:
        pad_width += [(0, 0)]
        window_shape = (r, c, d)

    # Pad the image.
    img = np.pad(img, pad_width=pad_width, mode='symmetric')

    # Extract patches as node features.
    try:
        import skimage
    except Exception:
        raise ImportError('Cannot import skimage, which is needed to '
                          'extract patches. Try to install it with '
                          'pip (or conda) install scikit-image.')
    patches = skimage.util.view_as_windows(img, window_shape=window_shape)
    patches = patches.reshape((h * w, r * c * d))
    return patches

def dispImg(img): 
    """
    This does the min-max scaling the images to 0 and 1 and displays the image.

    param img: The input image
    return None: Just displays the image in the notebook.
    """
    try:
        h, w, d = img.shape
        img_tmp = (img - np.min(img)) / (np.max(img) - np.min(img))
        plt.matshow(img_tmp)
        plt.show(block=False)
    except ValueError:
        try:
            h, w = img.shape
            img_tmp = (img - np.min(img)) / (np.max(img) - np.min(img))
            plt.matshow(img_tmp, cmap = "gray")
            plt.show(block=False)
        except ValueError:
            print("Image should be at least a 2D array.")
    return None  

def downsamplepcd(**kwargs):
    """
    This does the downsampling of pcd

    param position: The (N,3) matrix
    param texture: The (N,3) matrix
    param voxel_size: The small number < 1, should be adjusted acc downsampling requirement
    returns: The downsampled position and texture
    """
    p = kwargs["position"]
    t = kwargs["texture"]
    voxel_size = kwargs["voxel_size"]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(p)
    pcd.colors = o3d.utility.Vector3dVector(t)
    downpcd = pcd.voxel_down_sample(voxel_size)
    p = downpcd.points
    t = downpcd.colors
    return np.asarray(p), np.asarray(t)

def displayJSur(**kwargs):
    """
    Displays the pcd/mesh inside the Jupyter Notebook
    
    param position: The (N,3) matrix
    param texture: The (N,3) matrix
    """
    p = kwargs["position"]
    t = kwargs["texture"]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(p)
    pcd.colors = o3d.utility.Vector3dVector(t)
    visualizer = o3d.JVisualizer()
    visualizer.add_geometry(pcd)
    visualizer.show()
    return None

def displaySur(**kwargs):
    """
    Displays the pcd outside the Jupyter Notebook

    param position: The (N,3) matrix
    param texture: The (N,3) matrix
    """
    p = kwargs["position"]
    t = kwargs["texture"]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(p)
    pcd.colors = o3d.utility.Vector3dVector(t)
    o3d.visualization.draw_geometries([pcd]) 
    return None

def getPositionTexture(file_path):
    """
    Takes the input as pcd/mesh file and returns the vertices, texture, faces.
    """
    mesh = o3d.io.read_triangle_mesh(file_path)
    vertices = np.asarray(mesh.vertices)
    texture = np.asarray(mesh.vertex_colors) if len(np.asarray(mesh.vertex_colors)) != 0 else np.ones(vertices.shape)*0.5
    triangles = np.asarray(mesh.triangles)
    return (vertices, texture, triangles)


def dispMesh(**kwargs):
    """
    Displays the mesh outside the Jupyter environment
    """
    p = kwargs["position"]
    t = kwargs["texture"]
    f = kwargs["faces"]
    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(p)
    mesh.vertex_colors = o3d.utility.Vector3dVector(t)
    mesh.triangles = o3d.utility.Vector3iVector(f)
    o3d.visualization.draw_geometries([mesh])
    return None


def getDistPcd(texture):
    """
    To get the intial distance on the pcd, used in eikonal equation

    param texture: This input texture should mostly be zero except where you annotate (that is put seed)

    return mask: Wherever you did the annotation, the mask is  0 at that place  and 1 elsewhere.
    """
    mask = (texture[:,:] != 0).astype("int")
    mask = np.sum(mask, axis=1)
    mask[mask[:] == 0] = -1
    mask[mask[:] > 0] = 0
    mask[mask[:] == -1] = 1
    return mask

def getDist(img):
    """
    To get the intial distance on the image, used in eikonal equation used for example in segmentation.

    param img: This input img should mostly be zero except where you annotate (that is put seed) 
    return mask: Wherever you did the annotation, the mask is  0 at that place  and 1 elsewhere. 
    """
    mask = (img[:,:,:] != 0).astype("int")
    mask = np.sum(mask, axis=2)
    mask[mask[:,:] == 0] = -1
    mask[mask[:,:] > 0] = 0
    mask[mask[:,:] == -1] = 1
    return mask

def genInitialSeeds(**kwargs):
    """
    Generates the intial level-set, used for example in problems of semi-supervised classification.

    param labels: The (N,1) vector N being the number of samples to be classified.
    param num_seeds: The number of labels (semi-supervised instances) you want to put. 
    return Front: It is the list of len C, C being the number of classes, each element is front corresponding to a class of shape (N,1),
    wherever you put the labels, the value is 1 and -1 elsewhere. (Values inside the level-set = 1 and outside = -1)
    """
    labels = kwargs["labels"]
    num_seeds = kwargs["num_seeds"]

    M = []
    for i in range(np.max(labels)+1):
        mask = (labels == i)
        dist = np.ones(len(mask))
        M.append((mask,dist))

    Front = []
    for mTuple in M:
        j = 0
        for i in range(len(mTuple[0])):
            if j < num_seeds:
                if mTuple[0][i] == True:
                    mTuple[1][i] = -1
                    j = j+1
            else: break
        Front.append(-1 * np.reshape(mTuple[1], (len(mTuple[1]),1)))
    del M # not required
    print("Success!")
    return Front
    
from collections import namedtuple
#A simple structure to group the edge_index and edge_attr to create a graph.
Graph = namedtuple('Graph', 'edge_index, edge_attr')
