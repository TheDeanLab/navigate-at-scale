import os
import sys
# from navigate import __version__

sys.path.insert(0, os.path.abspath("../"))


# -- Project information -----------------------------------------------------

project = "navigate-at-scale"
copyright = "2023, Dean Lab, UT Southwestern Medical Center"
author = "Dean Lab, UT Southwestern Medical Center"

# The full version, including alpha/beta/rc tags
#release = __version__

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.coverage",
    "sphinx_toolbox.collapse",
    "sphinx.ext.autosectionlabel",
]

autosectionlabel_prefix_document = True
autosummary_generate = True
autoclass_content = "class"  # "both"
autodoc_member_order = "groupwise"
autodoc_default_flags = [
    "members",
    "inherited-members",
    "show-inheritance",
]

autodoc_inherit_docstrings = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["./_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# If true, the current module name will be prepended to all
# description unit titles (such as .. function::).
add_module_names = True

# The default language to highlight source code
highlight_language = "python"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_show_sphinx = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

html_logo = "../../plugin-icon.png"

pygments_style = "sphinx"

# -- LaTeX output options ----------------------------------------------------

latex_elements = {'preamble': r'''
                  \usepackage[utf8]{inputenc}
                  \usepackage{enumitem}
                  \setlistdepth{99}
                  \DeclareUnicodeCharacter{03BC}{$\mu$}
                  ''',
                  'extraclassoptions': 'openany,oneside'}

latex_documents = [
  ('index', 'navigate.tex', 'navigate-at-scale Documentation',
   'Dean Lab, UT Southwestern Medical Center', 'manual', True),
]

latex_domain_indices = False