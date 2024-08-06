# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PEAF'
copyright = '2024, 深圳市精艺信息技术有限公司'
author = 'Advisor'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
]
myst_enable_extensions = [
    "deflist",
]

source_suffix = {
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_book_theme"
html_static_path = ['_static']
html_title = "Practical Enterprise Architecture Framework"
html_theme_options = {
    "home_page_in_toc": True,
    "use_sidenotes": True,
}
