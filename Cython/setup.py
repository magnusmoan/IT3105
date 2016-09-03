from distutils.core import setup
from Cython.Build import cythonize
import Cython.Compiler.Options
from setuptools import Extension
Cython.Compiler.Options.annotate = True
extensions = [Extension("*", ["*.pyx"])]

setup(
        ext_modules = cythonize(extensions) 
        )
