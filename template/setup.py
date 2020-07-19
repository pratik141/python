#!/usr/bin/env python3

"""
Setup file_render
"""

from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    description='Load variables from YAML-formatted files to render a jinja2 template',
    url='https://github.com/pratik141/file_render',

    author='Pratik Anand',
    author_email='anandpratik141@gmail.com',

    license='GNU General Public License v3',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3',

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='jinja2 template',

    package_dir={'': 'file_render'},

    py_modules=[
        'file_render',
    ],

    install_requires=[
        'jinja2',
        'pyaml',
    ],

    extras_require={
    },

    package_data={
    },

    data_files=[
    ],

    entry_points={
        'console_scripts': [
            'file_render=file_render:main',
        ],
    },
)