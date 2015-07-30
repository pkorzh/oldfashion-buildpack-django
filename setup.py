#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow trove classifiers in previous python versions
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

def requireModules(moduleNames=None):
    import re
    if moduleNames is None:
        moduleNames = []
    else:
        moduleNames = moduleNames

    commentPattern = re.compile(r'^\w*?#')
    moduleNames.extend(
        filter(lambda line: not commentPattern.match(line),
            open('requirements.txt').readlines()))

    return moduleNames

scripts = [
    'buildpack=__init__:Buildpack',
]

setup(
    name='oldfashion-buildpack-django',

    version='1.0.0',

    author='Platon Korzh',
    author_email='platon@korzh.io',

    description='oldfashion buildpack for django',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers'
    ],

    install_requires=requireModules([

    ]),

    include_package_data = True,

    entry_points={'oldfashion.buildpack': scripts}
)
