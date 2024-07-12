# Configuration file for the Sphinx documentation builder.

import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = 'LLM-MRI'
copyright = '2024, Luiz Costa, Mateus Figenio, André Santanchè, Luiz Gomes-Jr'
author = 'Luiz Costa, Mateus Figenio, André Santanchè, Luiz Gomes-Jr'
release = '01.0'

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc"
]

html_theme = "classic"
html_static_path = ['_static']

# Include custom CSS file
def setup(app):
    app.add_css_file('custom.css')

html_theme_options = {
    'rightsidebar': False,
    'relbarbgcolor': 'black'
}
