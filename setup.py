import setuptools
from movens.about import (
    __package_name__,
    __version__,
    __description__,
    __email__,
    __author__,
    __github__,
    __keywords__,
    __development_status__,
    __programming_language__,
    __license__,
    __operating_system__,
    __intended_audience__,
    __python_requires__,
)

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
    keywords=__keywords__,
    packages=setuptools.find_packages(),
    classifiers=[
        f"Development Status :: {__development_status__}",
        f"Programming Language :: {__programming_language__}",
        f"License :: {__license__}",
        f"Operating System :: {__operating_system__}",
        f"Intended Audience :: {__intended_audience__}",
    ],
    python_requires=__python_requires__,
    entry_points={
        "console_scripts": [f"{__package_name__} = {__package_name__}.cli:main"],
    },
)
