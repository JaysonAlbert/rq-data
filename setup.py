#!/usr/bin/env python

from setuptools import setup, find_packages


try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''


setup(
    name='rq-data',
    version='0.01',
    description='rq data tools',
    long_description=long_description,
    author='Jie Wang',
    author_email='790930856@qq.com',
    url='https://github.com/JaysonAlbert/rq-data',
    packages=find_packages(include=['rq-data', 'rq-data.*']),

    install_requires=[
        'selenium',
        'pymongo'
    ]
)
