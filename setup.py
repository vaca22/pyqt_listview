from distutils.core import setup
import py2exe
from setuptools import find_packages

setup(
    windows=[{"script": "src/vaca/main.py"}],
    options={"py2exe": {"includes": []}},
    packages=['src/vaca']

)