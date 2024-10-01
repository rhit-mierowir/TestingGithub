# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
import toml

py_project_toml = os.path.join(os.getcwd(),"../../../pyproject.toml")
py_project_data = toml.load(py_project_toml)

#Load general data for website from pyproject.toml file
project = py_project_data["config"]["sphinx"]["name"]
copyright = py_project_data["config"]["sphinx"]["copyright_message"]
author = py_project_data["config"]["sphinx"]["author"]
release = py_project_data["tool"]["poetry"]["version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

directory_of_source_code = os.path.join(os.getcwd(),"../../../")
sys.path.append(directory_of_source_code)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = py_project_data["config"]["sphinx"]["theme"]
html_theme = 'sphinx_book_theme' # change html theme
#html_theme = 'sphinx_wagtail_theme'
#html_theme = 'sphinx_nefertiti'
#html_theme = 'pydata_sphinx_theme'

if (html_theme == 'sphinx_book_theme'):
    print("Selected Theme: {book}theme")
    pass # pip install sphinx-book-theme
elif (html_theme == 'sphinx_wagtail_theme'):
    print("Selected Theme: Wagtail")
    pass # pip install sphinx-wagtail-theme
    extensions.append("sphinx_wagtail_theme")
elif (html_theme == 'sphinx_nefertiti'):
    print("Selected Theme: Nefertiti")
    pass # pip install sphinx-nefertiti
elif (html_theme == 'pydata_sphinx_theme'):
    print("Selected Theme: PyData")
    pass # pip install pydata-sphinx-theme
else:
    print("HTML theme not recognized.")


html_static_path = ['_static']

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html

todo_include_todos=True             # True if want to see todos
todo_emit_warnings=False            # True if want warnings created for each todo item that exists

# -- Options for napoleon extension ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html

napoleon_google_docstring = False           # False to turn off support for google Docstrings
napoleon_numpy_docstring = True             # True to turn on support for numpy Docstrings
napoleon_include_init_with_doc = True       # True to include __init__ as it's own function if it has an a related docstring. If false, just append to class documentation.
napoleon_include_private_with_doc = True    # True to include private members with docstrings, false resorts to Sphinx's defaults
napoleon_include_special_with_doc = True    # True to include special members like __membername__ with docstrings in documentation. If false, Sphinx defaults, defalts to true.

