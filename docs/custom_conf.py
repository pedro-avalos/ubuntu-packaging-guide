import sys
sys.path.append('/usr/lib/python3/dist-packages')
import datetime
import distro_info

# Custom configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# The file is included in the common conf.py configuration file.
# You can modify any of the settings below or add any configuration that
# is not covered by the common conf.py file.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# If you're not familiar with Sphinx and don't want to use advanced
# features, it is sufficient to update the settings in the "Project
# information" section.

############################################################
### Project information
############################################################

# Product name
project = 'Ubuntu'
author = 'Canonical Group Ltd.'
version = '2.0-preview'

# The title you want to display for the documentation in the sidebar.
# You might want to include a version number here.
# To not display any title, set this option to an empty string.
html_title = project + ' documentation'

# The default value uses the current year as the copyright year.
#
# For static works, it is common to provide the year of first publication.
# Another option is to give the first year and the current year
# for documentation that is often changed, e.g. 2022–2023 (note the en-dash).
#
# A way to check a GitHub repo's creation date is to obtain a classic GitHub
# token with 'repo' permissions here: https://github.com/settings/tokens
# Next, use 'curl' and 'jq' to extract the date from the GitHub API's output:
#
# curl -H 'Authorization: token <TOKEN>' \
#   -H 'Accept: application/vnd.github.v3.raw' \
#   https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = '%s, %s' % (datetime.date.today().year, author)

## Open Graph configuration - defines what is displayed as a link preview
## when linking to the documentation from another website (see https://ogp.me/)
# The URL where the documentation will be hosted (leave empty if you
# don't know yet)
# NOTE: If no ogp_* variable is defined (e.g. if you remove this section) the
# sphinxext.opengraph extension will be disabled.
ogp_site_url = 'https://canonical-ubuntu-packaging-guide.readthedocs-hosted.com/'
# The documentation website name (usually the same as the product name)
ogp_site_name = 'Ubuntu Packaging Guide'
# The URL of an image or logo that is used in the preview
ogp_image = 'https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg'

# Update with the local path to the favicon for your product
# (default is the circle of friends)
html_favicon = '.sphinx/_static/favicon.png'

# (Some settings must be part of the html_context dictionary, while others
#  are on root level. Don't move the settings.)
html_context = {

    # Change to the link to the website of your product (without "https://")
    # For example: "ubuntu.com/lxd" or "microcloud.is"
    # If there is no product website, edit the header template to remove the
    # link (see the readme for instructions).
    'product_page': 'ubuntu.com',

    # Add your product tag (the orange part of your logo, will be used in the
    # header) to ".sphinx/_static" and change the path here (start with "_static")
    # (default is the circle of friends)
    'product_tag': '_static/tag.png',

    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    'discourse': 'https://discourse.ubuntu.com',

    # Change to the Mattermost channel you want to link to
    # (use an empty value if you don't want to link)
    'mattermost': '',

    # Change to the GitHub URL for your project
    'github_url': 'https://github.com/canonical/ubuntu-packaging-guide',

    # Change to the branch for this version of the documentation
    'github_version': version,

    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    'github_folder': '/docs/',

    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    'github_issues': 'enabled',

    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # You can override the default setting on a page-by-page basis by specifying
    # it as file-wide metadata at the top of the file, see
    # https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html
    'sequential_nav': "none"
}

# If your project is on documentation.ubuntu.com, specify the project
# slug (for example, "lxd") here.
slug = ""

############################################################
### Redirects
############################################################

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: 'explanation/old-name.html': '../how-to/prettify.html',
# You can also configure redirects in the Read the Docs project dashboard
# (see https://docs.readthedocs.io/en/stable/guides/redirects.html).
# NOTE: If this variable is not defined, set to None, or the dictionary is empty,
# the sphinx_reredirects extension will be disabled.
redirects = {}

############################################################
### Link checker exceptions
############################################################

# Links to ignore when checking links
linkcheck_ignore = [
    'http://127.0.0.1:8000',
    r"https://bugs\.launchpad\.net/ubuntu/\+bug/2",
    r"https?://localhost.+",
    r"ftp:.+",
    r"sftp:.+",
    r"news:.+",
    r"irc:.+",
    r"mailto:.+",
    r"jabber:noreply@launchpad\.net",
    r"http://www.example.com/.+",
    r"https://merges.ubuntu.com/.*",
    ]

# Pages on which to ignore anchors
# (This list will be appended to linkcheck_anchors_ignore_for_url)
custom_linkcheck_anchors_ignore_for_url = []

############################################################
### Additions to default configuration
############################################################

## The following settings are appended to the default configuration.
## Use them to extend the default functionality.

# NOTE: Remove this variable to disable the MyST parser extensions.
#custom_myst_extensions = []

# Add custom Sphinx extensions as needed. 
# This array contains recommended extensions that should be used.
# NOTE: The following extensions are handled automatically and do 
# not need to be added here: myst_parser, sphinx_copybutton, sphinx_design,
# sphinx_reredirects, sphinxcontrib.jquery, sphinxext.opengraph
custom_extensions = [
    #'sphinx_tabs.tabs',
    #'canonical.youtube-links',
    #'canonical.related-links',
    #'canonical.custom-rst-roles',
    #'canonical.terminal-output'
    ]

# Add custom required Python modules that must be added to the
# .sphinx/requirements.txt file.
# NOTE: The following modules are handled automatically and do not need to be
# added here: canonical-sphinx-extensions, furo, linkify-it-py, myst-parser,
# pyspelling, sphinx, sphinx-autobuild, sphinx-copybutton, sphinx-design,
# sphinx-reredirects, sphinx-tabs, sphinxcontrib-jquery, sphinxext-opengraph
custom_required_modules = []

# Add files or directories that should be excluded from processing.
custom_excludes = [
    'doc-cheat-sheet*',
    ]

# Add CSS files (located in .sphinx/_static/)
custom_html_css_files = []

# Add JavaScript files (located in .sphinx/_static/)
custom_html_js_files = []

## The following settings override the default configuration.

manpages_url = ("https://manpages.ubuntu.com/manpages/"
                f"{distro_info.UbuntuDistroInfo().stable()}/en/"
                "man{section}/{page}.{section}.html")

# Specify a reST string that is included at the end of each file.
# If commented out, use the default (which pulls the reuse/links.txt
# file into each reST file).
# custom_rst_epilog = ''

# By default, the documentation includes a feedback button at the top.
# You can disable it by setting the following configuration to True.
disable_feedback_button = False

# Add tags that you want to use for conditional inclusion of text
# (https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#tags)
custom_tags = []

############################################################
### Additional configuration
############################################################

## Add any configuration that is not covered by the common conf.py file.

# Define a :center: role that can be used to center the content of table cells.
rst_prolog = '''
.. role:: center
   :class: align-center

.. caution::

   The Packaging and Development guide is currently undergoing a major overhaul
   to bring it up to date. The current state you are seeing now is a preview of
   this effort.

   The current version is unstable (changing URLs can occur at any time) and
   most content is not in properly reviewed yet. Proceed with caution and be
   aware of technical inaccuracies.

   If you are an experienced packager and would like to contribute, we would
   love for you to be involved! See :doc:`our contribution page </contribute>`
   for details of how to join in.
'''

# The root toctree document.
root_doc = 'index'

# Sphinx-copybutton config options:
# 1) prompt to be stripped from copied code.
# 2) Set to copy all lines (not just prompt lines) to ensure multiline snippets
# can be copied even if they don't contain an EOF line.
copybutton_prompt_text = '$ '
copybutton_only_copy_prompt_lines = False

# -- Options for EPUB output -------------------------------------------------

epub_basename = 'ubuntu-packaging-guide'
epub_show_urls = 'no'

# -- Options for PDF output --------------------------------------------------

latex_additional_files = [
    "./.sphinx/fonts/Ubuntu-B.ttf",
    "./.sphinx/fonts/Ubuntu-R.ttf",
    "./.sphinx/fonts/Ubuntu-RI.ttf",
    "./.sphinx/fonts/UbuntuMono-R.ttf",
    "./.sphinx/fonts/UbuntuMono-RI.ttf",
    "./.sphinx/fonts/UbuntuMono-B.ttf",
    "./.sphinx/images/Canonical-logo-4x.png",
    "./.sphinx/images/front-page-light.pdf",
    "./.sphinx/images/normal-page-footer.pdf",
]

latex_engine = 'xelatex'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_documents = [
    (
        root_doc,
        'ubuntu-packaging-guide.tex',
        html_title,
        author,
        'manual',
        True,
    ),
]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'fncychap': '',
    'preamble': r'''
%\usepackage{charter}
%\usepackage[defaultsans]{lato}
%\usepackage{inconsolata}
\setmainfont[UprightFont = *-R, BoldFont = *-B, ItalicFont=*-RI, Extension = .ttf]{Ubuntu}
\setmonofont[UprightFont = *-R, BoldFont = *-B, ItalicFont=*-RI, Extension = .ttf]{UbuntuMono}
\usepackage[most]{tcolorbox}
\tcbuselibrary{breakable}
\usepackage{lastpage}
\usepackage{tabto}
\usepackage{ifthen}
\usepackage{etoolbox}
\usepackage{fancyhdr}
\usepackage{graphicx}
\usepackage{titlesec}
\usepackage{fontspec}
\usepackage{tikz}
\usepackage{changepage}
\usepackage{array}
\usepackage{tabularx}
\graphicspath{ {../../.sphinx/images/} }
\definecolor{yellowgreen}{RGB}{154, 205, 50}
\definecolor{title}{RGB}{76, 17, 48}
\definecolor{subtitle}{RGB}{116, 27, 71}
\definecolor{label}{RGB}{119, 41, 100}
\definecolor{copyright}{RGB}{174, 167, 159}
\makeatletter
\def\tcb@finalize@environment{%
  \color{.}% hack for xelatex
  \tcb@layer@dec%
}
\makeatother
\newenvironment{sphinxclassprompt}{\color{yellowgreen}\setmonofont[Color = 9ACD32, UprightFont = *-R]{UbuntuMono}}{}
\tcbset{enhanced jigsaw, colback=black, fontupper=\color{white}}
\newtcolorbox{termbox}{use color stack, breakable, colupper=white, halign=flush left}
\newenvironment{sphinxclassterminal}{\setmonofont[Color = white, UprightFont = *-R]{UbuntuMono}\sphinxsetup{VerbatimColor={black}}\begin{termbox}}{\end{termbox}}
\newcommand{\dimtorightedge}{%
  \dimexpr\paperwidth-1in-\hoffset-\oddsidemargin\relax}
\newcommand{\dimtotop}{%
  \dimexpr\height-1in-\voffset-\topmargin-\headheight-\headsep\relax}
\newtoggle{tpage}
\AtBeginEnvironment{titlepage}{\global\toggletrue{tpage}}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[R]{\thepage\ of \pageref*{LastPage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[R]{\thepage\ of \pageref*{LastPage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{titlepage}{%
    \fancyhf{}
    \fancyfoot[L]{\footnotesize \textcolor{copyright}{© 2024 Canonical Ltd. All rights reserved.}}
}
\newcommand\sphinxbackoftitlepage{\thispagestyle{titlepage}}
\titleformat{\chapter}[block]{\Huge \color{title} \bfseries\filright}{\thechapter .}{1.5ex}{}
\titlespacing{\chapter}{0pt}{0pt}{0pt}
\titleformat{\section}[block]{\huge \bfseries\filright}{\thesection .}{1.5ex}{} 
\titlespacing{\section}{0pt}{0pt}{0pt}
\titleformat{\subsection}[block]{\Large \bfseries\filright}{\thesubsection .}{1.5ex}{} 
\titlespacing{\subsection}{0pt}{0pt}{0pt}
\setcounter{tocdepth}{1}
\renewcommand\pagenumbering[1]{}
''',
    'sphinxsetup': 'verbatimwithframe=false, pre_border-radius=0pt, verbatimvisiblespace=\\phantom{}, verbatimcontinued=\\phantom{}',
    'extraclassoptions': 'openany,oneside',
    'maketitle': r'''
\begin{titlepage}
\begin{flushleft}
    \begin{tikzpicture}[remember picture,overlay]
    \node[anchor=south east, inner sep=0] at (current page.south east) {
    \includegraphics[width=\paperwidth, height=\paperheight]{front-page-light}
    };
    \end{tikzpicture}
\end{flushleft}

\vspace*{3cm}

\begin{adjustwidth}{8cm}{0pt}
\begin{flushleft}
    \huge \textcolor{black}{\textbf{}{\raggedright{Ubuntu Packaging Guide}}}
\end{flushleft}
\end{adjustwidth}

\vfill

\begin{adjustwidth}{8cm}{0pt}
\begin{tabularx}{0.5\textwidth}{ l l }
    \hspace{3cm}  & \textcolor{lightgray}{© 2024 Canonical Ltd.}  \\
    \hspace{3cm}  & \textcolor{lightgray}{All rights reserved.}   \\
    \hspace{3cm}  &                                               \\
    \hspace{3cm}  &                                               \\
                                 
\end{tabularx}
\end{adjustwidth}

\end{titlepage}
\RemoveFromHook{shipout/background}
\AddToHook{shipout/background}{
      \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=south west, align=left, inner sep=0] at (current page.south west) {
        \includegraphics[width=\paperwidth]{normal-page-footer}
      };
      \end{tikzpicture}
      \begin{tikzpicture}[remember picture,overlay]
      \node[anchor=north east, opacity=0.5, inner sep=35] at (current page.north east) {
        \includegraphics[width=4cm]{Canonical-logo-4x}
      };
      \end{tikzpicture}
    }
''',
}
