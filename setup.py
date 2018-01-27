# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='xdi-pandas',
    version='0.1.0',
    description='Read XDI files to Pandas dataframe',
    long_description=readme,
    author='Patrick Browne',
    author_email='pt.browne@gmail.com',
    url='https://github.com/ptbrowne/xdi-pandas',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

