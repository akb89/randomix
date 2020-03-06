#!/usr/bin/env python3
"""randomix setup.py.

This file details modalities for packaging the randomix application.
"""

from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='randomix',
    description='Generate random word embeddings',
    author=' Alexandre Kabbach',
    author_email='akb@3azouz.net',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.0',
    url='https://github.com/akb89/randomix',
    download_url='https://github.com/akb89/randomix',
    license='MIT',
    keywords=['word embeddings', 'random', 'hack'],
    platforms=['any'],
    packages=['randomix', 'randomix.logging', 'randomix.exceptions',
              'randomix.utils', 'randomix.core'],
    package_data={'randomix': ['logging/*.yml', 'resources/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'randomix = randomix.main:main'
        ],
    },
    install_requires=['pyyaml>=4.2b1'],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Software Development :: Libraries :: Python Modules'],
    zip_safe=False,
)
