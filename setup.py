# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

repository = 'https://github.com/ptbrowne/xdi-pandas'
version = '0.1.2'
setup(
    name='xdi-pandas',
    version=version,
    description='Read XDI files to Pandas dataframe',
    long_description=readme,
    author='Patrick Browne',
    author_email='pt.browne@gmail.com',
    url=repository,
    download_url='%s/archive/%s.tar.gz' % (repository, version),
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['pandas']
)

