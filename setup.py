#!/usr/bin/env python

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hookshot',
    packages=['hookshot'],
    version='0.1.0',
    description='hookshot aka PyAutoGUI-ng',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/vesche/hookshot',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    install_requires=[
        'mss',
        'pyobjc;platform_system=="Darwin"',
        'python-xlib;platform_system=="Linux"',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: Public Domain',
        'Programming Language :: Python'
    ]
)