#!/usr/bin/env python
"""Setup.py for robot_kit"""

import os

from setuptools import setup, find_packages

readme = open('README.md').read()

# Pull in the package info
package_name = 'robot_kit'
package = __import__(package_name)
version = package.__version__
author = package.__author__
email = package.__email__


# Data and Example Files
def get_files(dir_name):
    """Simple directory walker"""
    return [(os.path.join('.', d), [os.path.join(d, f) for f in files]) for d, _, files in os.walk(dir_name)]


setup(
    name=package_name,
    version=version,
    description='Robot Kit',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=author,
    author_email=email,
    url='https://github.com/SuperCowPowers/robot_kit',
    packages=find_packages(),
    include_package_data=True,
    data_files=get_files('data') + get_files('examples'),
    install_requires=[
    ],
    extras_require={
    },
    license='Apache',
    keywords='Zeek, Bro, Python, PCAP',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
