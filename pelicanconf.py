#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import os

AUTHOR = u'Saurabh Kumar'
SITENAME = u'Saurabh Kumar'
SITEURL = 'http://localhost:8000'
TAGLINE = u'Thoughts and Writings'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'
TYPOGRIFY = True

THEME = "theme/pelican-svbtle-responsive"

PLUGINS = [
    'pelican_commonmark',  # https://github.com/theskumar/pelican-commonmark
]


MD_EXTENSIONS = ['headerid(level=3)', 'toc', 'extra', 'admonition', 'nl2br']

# FILES_TO_COPY = (('extra/CNAME', 'CNAME'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

USER_LOGO_URL = 'https://1.gravatar.com/avatar/fc974e2829eac6e3512a9d7f82e04723?s=160'
TWITTER_USERNAME = '_theskumar'
GOOGLE_PLUS_PROFILE_URL = 'https://plus.google.com/+SaurabhKumar0/'

# Social widget
SOCIAL = (('Github', 'http://github.com/theskumar'),
          ('Twitter', 'http://twitter.com/_theskumar'),
          ('Google+', 'https://plus.google.com/+SaurabhKumar0/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
