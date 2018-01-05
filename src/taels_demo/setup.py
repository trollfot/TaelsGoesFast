# -*- coding: utf-8 -*-

import sys, os
from setuptools import setup, find_packages


version = '0.1'


setup(
    name='taels_demo',
    version=version,
    description="",
    long_description=""" """,
    classifiers=[],
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "cromlech.browser",
        "setuptools",
    ],
)
