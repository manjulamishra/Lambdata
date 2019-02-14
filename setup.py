#!/usr/bin/env python
"""
package setup/insert/installation and metadata for lambdata
"""

import setuptools
REQUIRED = [
        "numpy",
        "pandas",
        "scipy",
        "matplotlib",
        "sklearn"
        
]
with open ("README.md", "r") as fh:
    LONG_DESCRIPTION =fh.read()

setuptools.setup(
        name="Lambdata-manjulamishra",
        version="0.0.9",
        author="manjulamishra",
        description="A collection of Data Science helper funtions",
        long_description=LONG_DESCRIPTION,
        long_description_contect_type="text/markdown",
        url="https://github.com/manjulamishra/Lambdata",
        packages=setuptools.find_packages(),
        python_requires=">=3.5",
        install_requires=REQUIRED,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
            ]
)
