#!/usr/bin/env python
"""Settings for adamkrieger.ca"""

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Krieger'
SITENAME = u'adamkrieger.ca'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Winnipeg'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/adamkrieger'),
          ('github', 'https://github.com/adamkrieger'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#AK
DELETE_OUTPUT_DIRECTORY = False
THEME = "./themes/nest"
FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

#NEST
NEST_INDEX_HEAD_TITLE = u'Adam Krieger'
NEST_INDEX_HEADER_TITLE = u'Adam Krieger'
NEST_INDEX_HEADER_SUBTITLE = u'Notes on Delivering Software'
NEST_HEADER_LOGO = "/images/aklogo_relief.png"
NEST_HEADER_IMAGES = 'countertop.jpg'
