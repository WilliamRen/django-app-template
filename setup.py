# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals)

from setuptools import setup, find_packages

# Get app version
with open('{{ app_name }}/version.py', 'rb') as fp:
    g = {}
    exec(fp.read(), g)
    version = g['__version__']

# Get package list and make app name mapping
packages = find_packages(exclude=['*.tests'])

# Read README file
def readme():
    with open('README.rst', 'r') as fp:
        return fp.read()

# Setup
setup(
    name='{{ app_name }}',
    version=version,
    description='{{ app_name }}',  # Change it for a better description :)
    author='',
    author_email='',
    license='',
    url='',
    long_description=readme(),
    keywords='',
    install_requires=[
        'Django',
    ],
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
