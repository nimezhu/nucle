#!/usr/bin/env python
# Programmer : zhuxp


from __future__ import print_function
from distutils.core import setup
from setuptools import setup, find_packages
import codecs
import os
import sys
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
        return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                             version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


metadata = {

          'name':"nucle",
          'version':find_version('lib',"nucle",'__init__.py'),
          'description':"Python lib for Nucleome Browser (vis.nucleome.org)",
          'author':"Xiaopeng Zhu",
          'license':'GNU General Public License',
          'url':'http://github.com/nucleome/nucle',
          'author_email':"nimezhu@gmail.com",
          'packages':[
                    "nucle",
                    "nucle.cmd"
                    ],
          'package_dir':{"":"lib"},
          'platforms':'any',
          'scripts':[
                   "bin/nucle",
                   ],
          'package_data':{"":["README.md"]},
          'install_requires':['h5py>=2.9.0','gunicorn>=19.9.0','falcon>=2.0.0','falcon-cors>=1.1.7'],
}

def main():
    if not float(sys.version[:3])>3.5:
        sys.stderr.write("CRITICAL: Python version must be greater than or equal to 3.5!")
        sys.exit(1)
    dist=setup(**metadata)




    
if __name__=="__main__":
    main()

