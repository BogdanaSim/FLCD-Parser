"""Configuration file for the Sphinx documentation builder."""

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'SharedParser'
copyright = '2022, Bogdana Simionica, Stefan Stefanache'
author = 'Bogdana Simionica, Stefan Stefanache'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints'
]
