#!/usr/bin/env python3

# https://setuptools.pypa.io/en/latest/
# https://github.com/pypa/setuptools
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author="Kaan Keskin",
    author_email="kaantr@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Debian Package Repository Statistics (DPRS) Tool",
    entry_points={
        'console_scripts': [
            'dprs=dprs:cli_main',
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="dprs",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    version="1.0",
)
