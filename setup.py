#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open
from setuptools import setup, find_packages

# Get the long description from the README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

DISTNAME = 'ramp-leaderboard'
DESCRIPTION = "Minimal RAMP Leaderboard"
MAINTAINER = 'Mehdi CHerti'
MAINTAINER_EMAIL = 'mehdicherti@gmail.com'
URL = 'https://github.com/paris-saclay-cds/ramp-leaderboard'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/paris-saclay-cds/ramp-leaderboard'


if __name__ == "__main__":
    setup(
        name=DISTNAME,
        version='0.1',
        maintainer=MAINTAINER,
        include_package_data=True,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        download_url=DOWNLOAD_URL,
        long_description=long_description,
        zip_safe=False,  # the package can run out of an .egg file
        classifiers=[
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'License :: OSI Approved',
            'Programming Language :: Python',
            'Topic :: Software Development',
            'Topic :: Scientific/Engineering',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS'],
        install_requires=[
            'tabulate',
            'clize',
            'numpy',
            'pandas',
            'sigtools',
        ],
        platforms='any',
        packages=find_packages(),
        scripts=['ramp_leaderboard']
    )
