#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gustavo Sandoval'
SITENAME = u'AlmostBrooklyn'
SITETITLE = u'Gustavo Sandoval'
SITESUBTITLE = u'Industry Professor of Computer Science at NYU University'
SITEURL = ''

#TIMEZONE = 'Europe/Paris'
#DEFAULT_LANG = u'en'

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'America/Atikokan'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# new from gussand
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Sharing
TWITTER_USER = 'gussand'
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'false'
#GITHUB_USER = 'gussand'
#GITHUB_SHOW_USER_LINK = 'true'

# Search
SEARCH_BOX = True


# conf for Flex theme by Alexandre Vicenzi
#THEME = "~/pelican-themes/Flex"
ROBOTS = 'index, '

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (('blog', '/archives.html'),)
#          ('Research', 'http://gussand.github.io/research'))

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/gsandoval'),
          ('github', 'https://github.com/gussand'),
          ('twitter', 'https://twitter.com/gussand'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

#PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']
