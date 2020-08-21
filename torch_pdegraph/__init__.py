__version__ = "1.1.1"

def info():
    about = """
    Torch_pdegraph is a proof of concept that how one can solve PDEs on graphs using torch-geometric's Message Passing classes.
    """
    print(about)

__all__= [
        '__version__',
        'info',
        ]
