import setuptools
from movens.about import *

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__github__,
    keywords="filemover, movefiles, organizefiles, organizefiles, filemovergui, filemover-gui",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.1",
    entry_points={
        "console_scripts": ["movens = movens.cli:main"],
    },
)
