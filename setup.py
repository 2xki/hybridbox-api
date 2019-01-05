#!/usr/bin/env python
"""
    This file is part of hybridbox-api
    :copyright: (c) 2018 by Jakob Schreiner.
    :license: BSD, see LICENSE for more details.
"""

from setuptools import setup, find_packages
from sys import version_info

dependencies = ['requests']

setup(
    name='hybridbox',
    version='1.0',
    author='Jakob Schreiner',
    author_email='e48e13207341b6bffb7fb1622282247b@protonmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/python-webuntis/python-webuntis',
    license='new-style BSD',
    description='Bindings for Hybridbox API',
    long_description=open('README.rst').read(),
    install_requires=dependencies,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)