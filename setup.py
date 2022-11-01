import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filemover",
    version="1.0.5",
    author="CodePerfectPlus",
    author_email="deepak008@live.com",
    description="CLI tool to arrange files smartly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Py-Contributors/FileMoverGUI",
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
        "console_scripts": ["filemover = filemover.cli:main"],
    },
)
