# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'HDRi Maker'
copyright = '2024, Andrea Donati (Andrew_D)'
author = 'Andrea Donati (Andrew_D)'
release = '3.0.121'

import os, sys

sys.path.insert(0, os.path.abspath('../..'))

# Inseriamo il percorso al file conf.py:
sys.path.append(os.path.relpath(os.path.dirname(__file__)))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

from convert_json_updates_to_rst import update_changelog

update_changelog()

extensions = ['sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

os.path.join(os.path.relpath(os.path.dirname(__file__)), "docs", "_static", "_images", "logos",
"exa_logo_orange_512.png")


html_theme_path = ["_themes", ]

html_static_path = ['_static']

html_favicon = "extreme_addons_blue_32.ico"

# html_logo = os.path.join(html_static_path[0], "_images", "logos", "exa_logo_orange_512.png")

