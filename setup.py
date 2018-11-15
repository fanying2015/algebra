#!/usr/bin/env python

from distutils.core import setup

setup(name='algebra',
      version='1.0',
      description='A small algebra manipulatioin pakage',
      author='Fanying Tang',
      author_email='fanyingtang@gmail.com',
      url='',
      entry_points = {
        'console_scripts': ['algebra-product=algebra.cli:main'],
    }
     )