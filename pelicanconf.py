#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'theskumar'
SITENAME = u'Saurabh Kumar'
SITEURL = ''

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

THEME = os.path.join(os.path.expanduser('~') + "/pelican-themes/svbtle-responsive")

FILES_TO_COPY = (('extra/CNAME', 'CNAME'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()


# Social widget
SOCIAL = (('Github', 'http://github.com/theskumar'),
          ('Twitter', 'http://twitter.com/thes_kumar'),
          ('Google+', 'https://plus.google.com/115577985358125648809/'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
