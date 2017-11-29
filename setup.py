# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 07:27:30 2017

@author: William

"""


import sys
from codecs import open
from os import path

from cx_Freeze import setup, Executable

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst'), encoding='utf-8') as f:
    readme_description = f.read()


# GUI applications require a different base on Windows (the default is for a
# console application)
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Dependencies are automatically detected, but can be explicitly declared
options = {
    'build_exe': {
        'build_exe': 'Lodging Rate Calculator',
        'optimize': 2,
        'includes': [
            'atexit',
            'lodging_functions',
            'qt_persistence',
            'PyQt5'
            ],
        'include_files': ["Qt_plugins", ".\\Qt_plugins", "data.ini", ".\\data.ini"],
        'include_msvcr': True
        }
    }

executables = [
    Executable(script='qt_calculator.py', base=base, targetName="Lodging Rate Calculator")
    ]

setup(
        name='Lodging Rate Calculator',
        version='0.7.0',
        url='',
        license='LGPLv3',
        author='wey391',
        author_email='wey391@gmail.com',
        description='Simple gui interface for common lodging calculations',
        long_description=readme_description,
        options=options,
        executables=executables,
        classifiers=[

                  'Development Status :: 3 - Alpha',

                  'Intended Audience :: End Users/Desktop',

                  'Topic :: Office/Business :: Financial',

                  'License :: OSI Approved :: GNU LGPLv3',

                  'Programming Language :: Python :: 3.6',

                  ],
        keywords='simple Qt lodging rate calculator',
        install_requires=['pyqt5', "cx_freeze"],
        python_requires='~=3.3',
        package_data={'data.ini': ['data.ini'], 'Qt_plugins': ['Qt_plugins/*.ui']},
        py_modules=["lodging_functions", "qt_calculator", "qt_manipulation"]
)
