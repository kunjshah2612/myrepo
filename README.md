# uLBrain

uLBrain is a library that is used specifically for mapping 2 Datasets 

# How to build this library locally?

## Create the following file structure locally:

``` python
.PYPIRC
package/
   ├───uLBrain
        ├───__init__.py 
        └───mapSKU.py     
```
__init__.py is required to import the directory as a package, and should be empty.

mapSKU.py is a module within the package that could contain the logic
(functions, classes, constants, etc.) of your package.

.PYPIRC file contains the username as __token__ and password as the access token generated from PYPI portal(username -> Account Settings -> API Token -> Add API token)
```python
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = ##copy paste token from PYPI portal
```
## Creating the package files:

You will now add files that are used to prepare the project for distribution. When you’re done, the project structure will look like this:

``` python
.PYPIRC
package/

   ├───uLBrain
   │     ├───__init__.py 
   │     └───mapSKU.py     
   ├───LICENSE
   ├───README.md
   └───setup.py
```
#### Creating setup.py

setup.py tells frontend build tools like pip and build what backend tool to use to create distribution packages for your project

Open setup.py  and enter the following content.

```python
import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="uLBrain",
    version="0.0.1",
    author="example",
    author_email="author@abc.com",
    description="Library created to map two Dataset",
    long_description=long_description,
    long_description_content_type='text/markdown',
    readme = "README.md",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
    'pyspark',
    'spark'
]
)
```
name is the distribution name of your package.

version is the package version. 

authors is used to identify the author of the package; you specify a name and an email for each author. You can also list maintainers in the same format.

description is a short, one-sentence summary of the package.

readme is a path to a file containing a detailed description of the package. This is shown on the package detail page on PyPI. In this case, the description is loaded from README.md (which is a common pattern). There also is a more advanced table form described in the project metadata specification.

requires-python gives the versions of Python supported by your project. Installers like pip will look back through older versions of packages until it finds one that has a matching Python version.

classifiers gives the index and pip some additional metadata about your package. In this case, the package is only compatible with Python 3, is licensed under the MIT license, and is OS-independent. You should always include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on. For a complete list of classifiers, see https://pypi.org/classifiers/.

#### Creating README.md¶
Open README.md and enter the following content. You can customize this if you’d like.

```text
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```
#### Creating License
It’s important for every package uploaded to the Python Package Index to include a license. This tells users who install your package the terms under which they can use your package. Once you have chosen a license, open LICENSE and enter the license text. For example, if you had chosen the MIT license:
```text
Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
## Generating distribution archives
#### Write the below command in the terminal to build the wheel file

```bash
python setup.py bdist_wheel
```
After doing the above step the directory structure would look like as follows

``` python
├───build
│   ├───bdist.win-amd64
│   └───lib
│       └───uLBrain
├───dist
│    └───uLBrain-0.0.1-py3-none-any.whl
├───uLBrain
|      ├───__init__.py 
│      └───mapSKU.py 
├───uLBrain.egg-info
├───LICENSE
├───README.md
└───setup.py
```
#### Write the below command to upload the wheel file to the PYPI portal 

```bash
twine upload dist/*
```
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install uLBrain.

```bash
pip install uLBrain
```

## Usage
Write the below commands to install & import the library into Databrick Notebook

```python
# installing the library 
pip install uLBrain

# Import the library and module 
from uLBrain import mapSKU
df = mapSKU.getMaterialMappedAtSKULevel("HierarchySiriusLocalProduct")
display(df)
```