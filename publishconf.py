#!/usr/bin/env python
# -*- coding: utf-8 -*- #
'''
This file is only used if you use `make publish` or explicitly specify it as
your config file.
'''
from __future__ import absolute_import, unicode_literals

import os
import sys

# This must be before pelicanconf import
sys.path.append(os.curdir)

from pelicanconf import *  # noqa

SITEURL = 'https://saurabh-kumar.com/blog/'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "saurabhkumar"
GOOGLE_ANALYTICS = "UA-26681217-2"
COPY_TEXT_PLUS = True

PLUGINS += [
    'minify',  # https://github.com/rdegges/pelican-minify
]
