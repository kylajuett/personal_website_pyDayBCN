"""Sphinx configuration file"""
import os

# General configuration ------------------------------
project = "Personal website"
author = "Kyla Juett"
copyright = f"2023, {author}"
language = os.environ.get("WEBSITE_LANGUAGE", "en")
locale_dirs = ["locales"]
gettext_uuid = True
gettext_compact = False
templates_path = ["_templates"]

exclude_patterns = [
    ".DS_Store",
    "Thumbs.db",
    "README.md",
    "build",
    "gettext",
    "jupyter_execute",
    "**/.ipynb_checkpoints/*",
    ".virtual_documents/**",
    "*.html",
]

extensions = [
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "myst_nb",
    "sphinx_design",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "notfound.extension",
    "ablog",
]

# Extension configuration ----------------------------
## notfound extension -----------------
notfound_urls_prefix = ""

## Myst parser ------------------------
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]
myst_enable_extensions = [
    "colon_fence",
    "dollarmath",
    "linkify",
]
myst_url_schemes = ["mailto", "http", "https"]

## MyST-NB ----------------------------
nb_execution_mode = "off"

## ablog ------------------------------
blog_baseurl = f"https://exemple.oriolabrilpla.cat/{language}"
blog_path = "blog"
post_show_prev_next = False
fontawesome_included = True

## Intersphinx ------------------------
intersphinx_mapping = {
    "numpy": ("https://numpy.org/doc/stable/", None),
    "python": ("https://docs.python.org/3/", None),
}

# HTML output configuration --------------------------
html_theme = "sphinx_book_theme"
html_logo = "images/portrait_placeholder.png"
html_title = f"{author}'s website"
html_theme_options = {
    "repository_url": "https://github.com/kylajuett/personal_website_pyDayBCN",
    "repository_branch": "main",
    "home_page_in_toc": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
    "article_footer_items": "utterances.html",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/kylajuett", 
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        {
            "name": "Twitter/X",
            "url": "https://twitter.com/kylajuett", 
            "icon": "fa-brands fa-twitter",
            "type": "fontawesome",
            "attributes": {"rel": "me"},
        },
        {
            "name": "Orcid",
            "url": "https://orcid.org/0000-0002-1847-9481",
            "icon": "fa-brands fa-orcid",
            "type": "fontawesome",
        },
        {
            "name": "Atom Feed",
            "url": f"{blog_baseurl}/{blog_path}/atom.xml",
            "icon": "fa-solid fa-rss",
            "type": "fontawesome",
        },
    ],
    "article_header_start": ["toggle-primary-sidebar", "version-switcher"],
    "switcher": {
        "json_url": "https://raw.githubusercontent.com/OriolAbril/personal_website_example/main/switcher.json",
        "version_match": language,
    },
}
ablog_collections = ("author", "category", "tag")
blog_sidebar = ["navbar-logo.html", "icon-links.html", "sbt-sidebar-nav.html", "ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"]
html_sidebars = {
    "blog": blog_sidebar,
    "blog/*": blog_sidebar,
    **{f"blog/{collection}/**": blog_sidebar for collection in ablog_collections},
    "blog/posts/**":  ["navbar-logo.html", "icon-links.html", "sbt-sidebar-nav.html", "ablog/postcard.html", "ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
}
