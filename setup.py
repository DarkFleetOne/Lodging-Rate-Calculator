# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 07:27:30 2017

@author: William

"""


from codecs import open
from os import path

from setuptools import setup, find_packages

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst'), encoding='utf-8') as f:
    readme_description = f.read()

setup(
        name='lodging-calculator',
        version='0.7.0',
        packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
        url='',
        license='LGPLv3',
        author='wey391',
        author_email='wey391@gmail.com',
        description='Simple gui interface for common lodging calculations',
        long_description=readme_description,
        classifiers=[

                  'Development Status :: 3 - Alpha',

                  'Intended Audience :: End Users/Desktop',

                  'Topic :: Office/Business :: Financial',

                  'License :: OSI Approved :: GNU LGPLv3',

                  'Programming Language :: Python :: 3.6',

                  ],
        keywords='simple Qt lodging rate calculator',
        install_requires=['pyqt5'],
        python_requires='~=3.3',
        package_data={'data.ini': ['data.ini'], 'Qt_plugins': ['Qt_plugins/*.ui']},
        py_modules=["lodging_functions", "qt_calculator", "qt_persistence", "qt_manipulation"]
)


