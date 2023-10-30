import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="testuL",
    version="0.0.12",
    author="Kunj Shah",
    author_email="Kunj.Shah@unilever.com",
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