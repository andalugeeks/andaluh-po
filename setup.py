#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ts=4
###
# 
# Copyright (c) 2018-2019 Andalugeeks
# Authors:
# - J. Félix Ontañón <felixonta@gmail.com>

# -*- coding: utf-8 -*- 

from setuptools import setup

# read the contents of your README file
from os import path
import io
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='andaluh-po',
    version='0.0.1',
    description='Transliterate español (spanish) gettext po files to andaluz spelling proposals',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='J. Félix Ontañón',
    author_email='felixonta@gmail.com',
    url='https://andaluh.es',
    project_urls={
        "Source Code": "https://github.com/andalugeeks/andaluh-po"
    },
    platforms=['win32', 'linux2'],
    license='GNU LESSER GENERAL PUBLIC LICENSE',
    classifiers=[
        "Topic :: Text Processing",
        "Topic :: Software Development :: Internationalization",
        "Natural Language :: Spanish",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],

    install_requires=[
        "polib",
        "andaluh",
    ],

    scripts=['bin/andaluh-po']
)