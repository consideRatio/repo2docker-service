# Configuration file for Sphinx to build our documentation to HTML.
#
# Configuration reference: https://www.sphinx-doc.org/en/master/usage/configuration.html
#
import datetime
import sys
from os.path import dirname

# -- Project information -----------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#
project = "repo2docker-service"
copyright = f"{datetime.date.today().year}, Project Jupyter Contributors"
author = "Project Jupyter Contributors"


# -- Setup system path for autodoc extensions --------------------------------
#
# We use autodoc to generate documentation in reference/, so we configure the
# system path to help autodoc detect the binderhub module.
#
git_repo_root = dirname(dirname(dirname(__file__)))
sys.path.insert(0, git_repo_root)


# -- General Sphinx configuration ---------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#
# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
#
extensions = [
    "autodoc_traits",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]
root_doc = "index"
source_suffix = [".md", ".rst"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#
html_logo = "_static/images/logo/logo.png"
html_favicon = "_static/images/logo/favicon.ico"
html_static_path = ["_static"]

# sphinx_book_theme reference: https://sphinx-book-theme.readthedocs.io/en/latest/?badge=latest
html_theme = "sphinx_book_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "repository_url": "https://github.com/consideratio/repo2docker-service/",
    "repository_branch": "main",
    "path_to_docs": "docs/source",
    "use_download_button": False,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
}


# -- Options for linkcheck builder -------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder
#
linkcheck_ignore = [
    r"(.*)github\.com(.*)#",  # javascript based anchors
    r"(.*)/#%21(.*)/(.*)",  # /#!forum/jupyter - encoded anchor edge case
    r"https://github.com/[^/]*$",  # too many github usernames / searches in changelog
    "https://github.com/consideratio/repo2docker-service/pull/",  # too many PRs in changelog
    "https://github.com/consideratio/repo2docker-service/compare/",  # too many comparisons in changelog
]
linkcheck_anchors_ignore = [
    "/#!",
    "/#%21",
]


# -- Options for the opengraph extension -------------------------------------
# ref: https://github.com/wpilibsuite/sphinxext-opengraph#options
#
# ogp_site_url is set automatically by RTD
ogp_image = "_static/logo.png"
ogp_use_first_image = True


# -- Options for the rediraffe extension -------------------------------------
# ref: https://github.com/wpilibsuite/sphinxext-rediraffe#readme
#
# This extensions help us relocated content without breaking links. If a
# document is moved internally, we should configure a redirect like below.
#
rediraffe_branch = "main"
rediraffe_redirects = {
    # "old-file": "new-folder/new-file-name",
}
