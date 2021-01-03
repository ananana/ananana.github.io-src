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
#THEME = 'backdrop'
THEME = 'themes/waterspill'
# specific theme (backdrop) configuration
PROFILE_IMAGE = '/images/portrait_AnaUban.JPG'
BACKDROP_IMAGE = '/images/public-domain-images-free-stock-photos-high-quality-resolution-downloads-around-the-house-7.jpg'
SITE_DESCRIPTION= 'Software developer and researcher; Natural language processing and machine learning PhD student; Python software developer / freelancer; Enthusiastic about AI, education, language, ideas'
EMAIL = 'ana.uban+prof@gmail.com'
BLOGKEYWORDS = ('machine learning', 'natural language processing', 'python', 'NLP', 'ML', 'deep learning', 'freelance', 'remote', 'contractor')

PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')

# Blogroll
LINKS = (('Human Language Technologies Research Center', 'http://nlp.unibuc.ro'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/ana-uban/'),
            ('UpWork', 'https://www.upwork.com/freelancers/~01f657838909aba2bf'),
            ('AngelList','https://angel.co/ana-sabina-uban'),
            ('Academic', 'http://nlp.unibuc.ro/people/anauban.html')
          # ('Another social link', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
