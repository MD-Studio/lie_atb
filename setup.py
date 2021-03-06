#! /usr/bin/env python
# -*- coding: utf-8 -*-

# package: mdstudio_atb
# file: setup.py
#
# Part of ‘mdstudio_atb’, a package providing access to the Automatic Topology
# Builder server https://atb.uq.edu.au using a Python API.
#
# Copyright © 2016 Marc van Dijk, VU University Amsterdam, the Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

distribution_name = 'mdstudio_atb'

setup(
    name=distribution_name,
    version=1.0,
    description='MDStudio component wrapping API access to the Automatic Topology Builder server',
    author="""
    Marc van Dijk - VU University - Amsterdam
    Paul Visscher - Zefiros Software (www.zefiros.eu)
    Felipe Zapata - eScience Center (https://www.esciencecenter.nl/)""",
    url='https://github.com/MD-Studio/MDStudio_atb',
    license='Apache Software License 2.0',
    keywords='LIEStudio ATB topology molecular force fields',
    platforms=['Any'],
    packages=find_packages(),
    package_data={distribution_name: ['schemas/endpoints/*']},
    py_modules=[distribution_name],
    install_requires=['requests', 'PyYAML'],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ]
)
