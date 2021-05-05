# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in rangsutra/__init__.py
from rangsutra import __version__ as version

setup(
	name='rangsutra',
	version=version,
	description='rangsutra_app',
	author='rangsutra_app',
	author_email='rangsutra_app@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
