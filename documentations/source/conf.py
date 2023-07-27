# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

from pathlib import Path

# django path directory
# sys.path.insert(0, os.path.abspath("../src")) # path relatif

_this_filepath = Path(os.path.realpath(__file__))
_apps_dirpath = _this_filepath.parent.parent.parent / "src"
sys.path.insert(0, str(_apps_dirpath))

# Setup Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
django.setup()

project = 'Visiopompe'
copyright = 'Nicolas RENARD, 2022'
author = 'Nicolas RENARD'
release = 'v1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',

]

templates_path = ['_templates']
exclude_patterns = ['_build']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
# html_theme_path = ["_themes", ]
html_logo = "_static/logo_visiopompe.jpg"

# -- Options for autodoc ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

# Automatically extract typehints when specified and place them in
# descriptions of the relevant function/method.
autodoc_typehints = "description"

# Don't show class signature with the class' name.
autodoc_class_signature = "separated"

#--Napoleon--
napoleon_google_docstring = True
napoleon_numpy_docstring = False
