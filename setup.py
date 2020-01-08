from setuptools import setup, find_namespace_packages

setup(
    name='raythena-plugins-example',
    version='1.0',
    author='Julien Esseiva',
    author_email='julien.esseiva@hefr.ch',
    packages=find_namespace_packages(include=['raythena.*'])
)
