import pathlib
from setuptools import setup, find_packages

HERE =  pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

install_requires = [
    'torch',
    'numpy',
    'mnist',
    'tqdm',
    'scipy',
    'scikit-learn',
    'scikit-image',
    'matplotlib',
    'opencv-python',
    'open3d-python',
]

setup(
    name="torch_pdegraph",
    version="1.0.0",
    description="Running paritial difference equations (PDEs) on graphs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/aGIToz/Pytorch_pdegraph",
    python_requires='>=3.6',
    install_requires=install_requires,
    packages=find_packages(),
    author="Amitoz AZAD",
    author_email="amitoz.sudo@gmail.com",
    license="MIT",
    include_package_data=True,
    )
