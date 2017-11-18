#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ana Sabina Uban'
SITENAME = u'Ana Sabina Uban'
SITEURL = 'https://ananana.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'themes']
THEME_STATIC_PATHS = ['pelican-themes']

# THEME = 'themes/pelican-alchemy/alchemy'
THEME = 'backdrop'
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ana-uban/'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
