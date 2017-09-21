# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2016, Anaconda, Inc. All rights reserved.
#
# Licensed under the terms of the BSD 3-Clause License.
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
"""Setup script."""

# Standard library imports
import ast
import os

# Third party imports
from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))
REQUIREMENTS = ['tornado >= 4.2']


def get_version(module='loghub'):
    """Get version."""
    with open(os.path.join(HERE, module, 'version.py'), 'r') as f:
        data = f.read()
    lines = data.split('\n')
    for line in lines:
        if line.startswith('VERSION_INFO'):
            version_tuple = ast.literal_eval(line.split('=')[-1].strip())
            version = '.'.join(map(str, version_tuple))
            break
    return version


def get_description():
    """Get long description."""
    with open(os.path.join(HERE, 'README.md'), 'r') as f:
        data = f.read()
    return data


setup(
    name='anaconda-project',
    version=get_version(),
    keywords=["conda anaconda project reproducible data science"],
    url='http://github.com/Anaconda-Server/anaconda-project',
    license='New BSD',
    author="Anaconda, Inc",
    author_email='info@anaconda.com',
    maintainer='Anaconda, Inc',
    maintainer_email='info@anaconda.com',
    description='Library to load and manipulate project directories',
    long_description=get_description(),
    zip_safe=False,
    install_requires=REQUIREMENTS,
    scripts=[
        'bin/anaconda-project'
    ],
    entry_points={
        'console_scripts': [
            'anaconda-project = anaconda_project.cli:main',
        ]
    },
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    #    packages=[
    #        'anaconda_project', 'anaconda_project.internal',
    #        'anaconda_project.internal.cli',
    #        'anaconda_project.requirements_registry',
    #        'anaconda_project.requirements_registry.providers',
    #        'anaconda_project.requirements_registry.requirements'
    #    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent', 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6'
    ])
