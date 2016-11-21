#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# flake8: noqa

from __future__ import unicode_literals

AUTHOR = 'elliot'
SITENAME = 'postsneakernet'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'
STATIC_PATHS = ['files']

ARTICLE_PATHS = ['articles']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}'

AUTHOR_URL = 'author/{slug}'
PAGE_URL = 'pages/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'

CATEGORIES_URL = 'categories'
TAGS_URL = 'tags'
ARCHIVES_URL = 'archives'

THEME = "/home/vagrant/pelican-themes/tuxlite_tbs"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/postsneakernet'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
