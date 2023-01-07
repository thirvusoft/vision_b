from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vision_b/__init__.py
from vision_b import __version__ as version

setup(
	name="vision_b",
	version=version,
	description="Lab test and Template development",
	author="thirvusoft",
	author_email="ts@gmail.com.",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
