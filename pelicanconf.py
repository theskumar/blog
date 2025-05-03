AUTHOR = "Saurabh Kumar"
SITENAME = "Saurabh Kumar's Blog"
SITEURL = ""

THEME = "themes/built-texts"
PATH = "content"

TIMEZONE = "Asia/Kolkata"

DEFAULT_LANG = "en"

TYPOGRIFY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {
            "css_class": "highlight",
            "guess_lang": False,
        },
        "markdown.extensions.meta": {},
        "markdown.extensions.extra": {},
        "markdown.extensions.admonition": {},
        "markdown.extensions.nl2br": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.sane_lists": {},
    },
    "output_format": "html5",
}

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# )

# Social widget
SOCIAL = (
    ("Github", "https://github.com/theskumar"),
    ("Twitter/X", "https://twitter.com/_theskumar"),
    ("Mastodon", "https://mastodon.social/@theskumar"),
)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
