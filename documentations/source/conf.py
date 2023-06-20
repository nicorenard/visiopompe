# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
from pathlib import Path

import django

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
release = 'v1.0'

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
html_theme_path = ["_themes", ]
html_logo = "_static/logo_visiopompe.jpg"
html_theme_options = {

    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

#rinoh pdf
rinoh_documents = [
    {
    'doc': 'index',
    'target': f'{project}',
    'title': project,
    'author': author,
    },

]

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
