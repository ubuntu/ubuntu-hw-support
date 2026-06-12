import datetime
import os
import sys
import yaml

from docutils.parsers.rst import roles
from sphinx.util.docutils import SphinxRole
from docutils import nodes

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# If you're new to Sphinx and don't want any advanced or custom features,
# just go through the items marked 'TODO'.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Our starter pack uses the custom Canonical Sphinx extension
# to keep all documentation based on it consistent and on brand:
# https://github.com/canonical/canonical-sphinx

#######################
# Project information #
#######################

# Project name
project = "Ubuntu hardware support"
author = "Canonical Ltd."

# Sidebar documentation title; best kept reasonably short
#  To include a version number, add it here (hardcoded or automated).
#  To disable the title, set to an empty string.
html_title = project + " documentation"

# Copyright string; shown at the bottom of the page
#
# Now, the starter pack uses CC-BY-SA as the license
# and the current year as the copyright year.
#
#  If your docs need another license, specify it instead of 'CC-BY-SA'.
#
#  If your documentation is a part of the code repository of your project,
#       it inherits the code license instead; specify it instead of 'CC-BY-SA'.
#
# NOTE: For static works, it is common to provide the first publication year.
#       Another option is to provide both the first year of publication
#       and the current year, especially for docs that frequently change,
#       e.g. 2022–2023 (note the en-dash).
#
#       A way to check a repo's creation date is to get a classic GitHub token
#       with 'repo' permissions; see https://github.com/settings/tokens
#       Next, use 'curl' and 'jq' to extract the date from the API's output:
#
#       curl -H 'Authorization: token <TOKEN>' \
#         -H 'Accept: application/vnd.github.v3.raw' \
#         https://api.github.com/repos/canonical/<REPO> | jq '.created_at'
copyright = f"{datetime.date.today().year}, Canonical Ltd"

# Documentation website URL
#  Update with the official URL of your docs or leave empty if unsure.
# NOTE: The Open Graph Protocol (OGP) enhances page display in a social graph
#       and is used by social media platforms; see https://ogp.me/
ogp_site_url = f"https://ubuntu.com/hardware/docs/"

# Preview name of the documentation website
#  To use a different name for the project in previews, update as needed.
ogp_site_name = project

# Preview image URL
#  To customise the preview image, update as needed.
ogp_image = "https://assets.ubuntu.com/v1/cc828679-docs_illustration.svg"

# Product favicon; shown in bookmarks, browser tabs, etc.
#  To customise the favicon, uncomment and update as needed.
# html_favicon = '.sphinx/_static/favicon.png'

# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context

html_context = {
    "product_page": "docs.ubuntu.com",
    #
    # Product tag image; the orange part of your logo, shown in the page header
    #  To add a tag image, uncomment and update as needed.
    # 'product_tag': '_static/tag.png',
    #
    # Your Discourse instance URL
    #  Change to your Discourse instance URL or leave empty.
    # NOTE: If set, adding ':discourse: 123' to an .rst file
    #       will add a link to Discourse topic 123 at the bottom of the page.
    "discourse": "https://discourse.ubuntu.com",
    #
    # Your Mattermost channel URL
    #  Change to your Mattermost channel URL or leave empty.
    "mattermost": "",
    #
    # Your Matrix channel URL
    #  Change to your Matrix channel URL or leave empty.
    "matrix": "https://matrix.to/#/#documentation:ubuntu.com",
    #
    # Your documentation GitHub repository URL
    #  Change to your documentation GitHub repository URL or leave empty.
    # NOTE: If set, links for viewing the documentation source files
    #       and creating GitHub issues are added at the bottom of each page.
    "github_url": "https://github.com/canonical/ubuntu-hw-support",
    #
    # Docs branch in the repo; used in links for viewing the source files
    #  To customise the branch, uncomment and update as needed.
    "repo_default_branch": "main",
    #
    # Docs location in the repo; used in links for viewing the source files
    #  To customise the directory, uncomment and update as needed.
    "repo_folder": "/docs/",
    #
    #  To enable or disable the Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # "sequential_nav": "both",
    #
    #  To enable listing contributors on individual pages, set to True
    "display_contributors": False,
    #
    # Required for feedback button
    "github_issues": "enabled",
    #
    "author": author,
    #
    "license": {
        "name": "CC-BY-SA-4.0",
        "url": "https://creativecommons.org/licenses/by-sa/4.0/",
    },
}

html_extra_path = []

# Allow opt-in build of the OpenAPI "Hello" example so docs stay clean by default.
if os.getenv("OPENAPI", ""):
    tags.add("openapi")  # noqa: F821
    html_extra_path.append("how-to/assets/openapi.yaml")

#  To enable the edit button on pages, uncomment and change the link to a
# public repository on GitHub or Launchpad. Any of the following link domains
# are accepted:
# - https://github.com/example-org/example"
# - https://launchpad.net/example
# - https://git.launchpad.net/example
#
html_theme_options = {
    "source_edit_link": "https://github.com/canonical/ubuntu-hw-support",
}

# Project slug; see https://meta.discourse.org/t/what-is-category-slug/87897
# TODO: If your documentation is hosted on https://docs.ubuntu.com/,
#       uncomment and update as needed.
slug = 'hardware/docs'

#######################
# Sitemap configuration: https://sphinx-sitemap.readthedocs.io/
#######################

# Use RTD canonical URL to ensure duplicate pages have a specific canonical URL
html_baseurl = f"https://ubuntu.com/hardware/docs/"

# URL scheme. Add language and version scheme elements.
sitemap_url_scheme = "{link}"

# Include `lastmod` dates in the sitemap:
sitemap_show_lastmod = True

# Exclude generated pages from the sitemap:
sitemap_excludes = [
    "404/",
    "genindex/",
    "search/",
]

sitemap_filename = "doc-sitemap.xml"

#  Add more pages to sitemap_excludes if needed. Wildcards are supported.
#  For example, to exclude module pages generated by autodoc, add '_modules/*'.

#######################
# Template and asset locations
#######################

html_static_path = ["_static"]
templates_path = [".sphinx/_templates"]

#############
# Redirects #
#############

# Add redirects to the 'redirects.txt' file
# https://sphinxext-rediraffe.readthedocs.io/en/latest/

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

# Rediraffe (internal) redirects
# ------------------------------

rediraffe_branch = "main"
rediraffe_redirects = "redirects.txt"

# Strips '/index.html' from destination URLs when building with 'dirhtml'
rediraffe_dir_only = True

###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
#
#  Remove or adjust the ACME entry after you update the contributing guide
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://www.gnu.org/software/grub/",
    "https://linux-sunxi.org/Ethernet",
    "https://frame.work/de/en/products/deep-computing-risc-v-mainboard",
    "https://www.kickstarter.com/projects/starfive/visionfive-2-lite-unlock-risc-v-sbc-at-199",
    r"https:\/\/www.microchip.com\/.*",
    r".*\/_images\/",
]

# A regex list of URLs where anchors are ignored by 'make linkcheck'
linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]

# give linkcheck multiple tries on failure
# linkcheck_timeout = 30
linkcheck_retries = 3

########################
# Configuration extras #
########################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
#
# NOTE: By default, the following MyST extensions are enabled:
#       substitution, deflist, linkify
# myst_enable_extensions = set()

# Append the path for the ubuntu_images extension; remove this if/when the
# sphinx_ubuntu_images package is brought up to date
sys.path.append("./_ext")

# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
# NOTE: The canonical_sphinx extension is required for the starter pack.
extensions = [
    "canonical_sphinx",
    "notfound.extension",
    "sphinx_design",
    "sphinx_rerediraffe",
    "sphinx_reredirects",
    "sphinx_tabs.tabs",
    "sphinxcontrib.jquery",
    "sphinxext.opengraph",
    "sphinx_config_options",
    "sphinx_contributor_listing",
    "sphinx_filtered_toctree",
    "sphinx_related_links",
    "sphinx_roles",
    "sphinx_terminal",
    # "sphinx_ubuntu_images",
    "sphinx_youtube_links",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    # Extensions for this docs set:
    "sphinx-prompt",
    "sphinx.ext.extlinks",
    "ubuntu_images",
]

# Excludes files or directories from processing
exclude_patterns = [".venv"]

# Adds custom CSS files, located under 'html_static_path'
html_css_files = ["https://assets.ubuntu.com/v1/d86746ef-cookie_banner.css"]

# Adds custom JavaScript files, located under 'html_static_path'
html_js_files = [
    "js/overwrite_links.js",
    "https://assets.ubuntu.com/v1/287a5e8f-bundle.js",
]

# Specifies a reST snippet to be appended to each .rst file
rst_epilog = """
.. include:: /reuse/links.txt
.. include:: /reuse/substitutions.txt
"""

# Feedback button at the top; enabled by default
#
#  To disable the button, uncomment this.
# disable_feedback_button = True

# Your manpage URL
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.
manpages_url = (
    'https://manpages.ubuntu.com/manpages/resolute/en/'
    'man{section}/{page}.{section}.html'
)

# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.
rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2
.. role:: woke-ignore
    :class: woke-ignore
.. role:: vale-ignore
    :class: vale-ignore
"""

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34
if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"

# Workaround for substitutions.yaml
if os.path.exists("./reuse/substitutions.yaml"):
    with open("./reuse/substitutions.yaml", "r") as fd:
        myst_substitutions = yaml.safe_load(fd.read())

# Add configuration for intersphinx mapping
intersphinx_mapping = {
    "subiquity": ("https://canonical-subiquity.readthedocs-hosted.com/en/latest", None),
    "cloudinit": ("https://cloudinit.readthedocs.io/en/latest/", None),
}

# Set up some simple aliases for bugs and packages
extlinks = {
    "lp-bug": ("https://bugs.launchpad.net/bugs/%s", "LP: #%s"),
    "lp-pkg": ("https://launchpad.net/ubuntu/+source/%s", "%s"),
}


# Redefine the Sphinx 'command' role to behave/render like 'literal'
class CommandRole(SphinxRole):
    def run(self):
        text = self.text
        node = nodes.literal(text, text)
        return [node], []


def setup(app):
    roles.register_local_role("command", CommandRole())


# Define a custom role for package-name formatting
def pkg_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.literal(rawtext, text)
    return [node], []


roles.register_local_role("pkg", pkg_role)
