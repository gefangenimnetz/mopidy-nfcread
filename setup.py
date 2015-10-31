from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='Mopidy-NFCread',
    version=get_version('mopidy_nfcread/__init__.py'),
    url='https://github.com/gefangenimnetz/mopidy-nfcread',
    license='Apache License, Version 2.0',
    author='Florian Kutschera',
    author_email='kontakt@florian-kutschera.de',
    description='Extension for selecting a playable uri (e.g. local, spotify, etc) via NFC tag and reader',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'nfcread = mopidy_nfcread:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
