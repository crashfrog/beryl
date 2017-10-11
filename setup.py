#!/usr/bin/env python
from distutils.core import setup
import setuptools

description = '''


'''

setup(
	name='beryl',
	version='0.1a',
	description=description,
	url='',
	author='Justin Payne',
	author_email='justin.payne@fda.hhs.gov',
	license='CC0 1.0',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Science/Research',
		'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
		'Topic :: Utilities'
	],
	keywords='research bioinformatics',
	packages=setuptools.find_packages(),
	install_requires=['ipfsapi>=0.4.2', 'docpie>=0.3.6', 'pycapnp>=0.6.1', 'halo>=0.0.7'],
	python_requires='>=3.4',
	entry_points=dict(console_scripts=[
		'beryl = beryl-cli.__main__:main',
		'beryld-setup = beryl.installation:install_service',
	])
)