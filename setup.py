#!/usr/bin/env python

import hookshot
from setuptools import setup

setup(
    name='hookshot',
    packages=['hookshot'],
    version=hookshot.__version__,
    description='hookshot',
    license='WTFPL',
    url='https://github.com/vesche/hookshot',
    author='Austin Jackson',
    author_email='vesche@protonmail.com',
    entry_points={
        'console_scripts': [
            'hookshot = hookshot.hookshot:main',
        ]
    },
    install_requires=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: Public Domain",
        "Programming Language :: Python"
    ]
)