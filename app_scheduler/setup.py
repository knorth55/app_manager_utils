#!/usr/bin/env python

from catkin_pkg.python_setup import generate_distutils_setup
from distutils.core import setup
from setuptools import find_packages


d = generate_distutils_setup(
    packages=find_packages('src'),
    package_dir={'': 'src'},
)

setup(**d)
