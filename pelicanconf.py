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
# specific theme (backdrop) configuration
PROFILE_IMAGE = '/images/portrait_AnaUban.JPG'
BACKDROP_IMAGE = '/images/public-domain-images-free-stock-photos-high-quality-resolution-downloads-around-the-house-7.jpg'
SITE_DESCRIPTION= 'Software developer and researcher; Natural language processing and machine learning PhD student; Python software developer / freelancer; Enthusiastic about AI, education, language, ideas'
EMAIL = 'ana.uban@gmail.com'

PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ana-uban/'),
            ('upwork (freelance)', 'https://www.upwork.com/freelancers/~01f657838909aba2bf'),
          # ('Another social link', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
