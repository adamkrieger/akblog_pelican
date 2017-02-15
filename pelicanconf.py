#!/usr/bin/env python
"""Settings for adamkrieger.ca"""

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Adam Krieger'
SITENAME = u'adamkrieger.ca'
SITEURL = 'http://www.adamkrieger.ca'
DISQUS_SITEURL = "http://www.adamkrieger.ca"

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
LINKS = ()
#('Pelican', 'http://getpelican.com/')

# Social widget
SOCIAL = (
    (
        '<i class="fa fa-twitter-square icon-social" aria-hidden="true"></i> @adamkrieger',
        'https://twitter.com/adamkrieger'),
    (
        '<i class="fa fa-github-square icon-social" aria-hidden="true"></i> /AdamKrieger',
        'https://github.com/adamkrieger'),
    (
        '<i class="fa fa-linkedin-square icon-social" aria-hidden="true"></i> Adam Krieger',
        'https://www.linkedin.com/in/adam-krieger-7a087048/')
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#AK
DELETE_OUTPUT_DIRECTORY = False
THEME = "./themes/nest"
FILENAME_METADATA = r"(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)"
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True
GOOGLE_ANALYTICS = 'UA-66645426-1'
TWITTER_HANDLE = 'AdamKrieger'
DISQUS_SITENAME = 'adamkrieger'

#NEST
NEST_INDEX_HEAD_TITLE = u'Adam Krieger'
NEST_INDEX_HEADER_TITLE = u'Adam Krieger'
NEST_INDEX_HEADER_SUBTITLE = u'Notes on Delivering Software'
NEST_HEADER_LOGO = "/images/aklogo_relief.png"
NEST_HEADER_IMAGES = 'countertop.jpg'

NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'), ('Tags', '/tags.html')]
NEST_INDEX_CONTENT_TITLE = u'Posts'
NEST_COPYRIGHT = u'&copy; adamkrieger.ca 2017'

# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Post Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'History of Opinion'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tag List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'#Hashtag'
NEST_TAGS_CONTENT_TITLE = u'Tags'
NEST_TAGS_CONTENT_LIST = u'tagged'
