from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in labour_welfare/__init__.py
from labour_welfare import __version__ as version

setup(
	name='labour_welfare',
	version=version,
	description='Labour Welfare',
	author='Sumit',
	author_email='sumit.k@indictranstech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
