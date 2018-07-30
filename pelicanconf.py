#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diego Mungu\xeda'
SITENAME = u'Diego Mungu\xeda'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'es'

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
SOCIAL = (('twitter', 'http://twitter.com/diegomunguia'),
          ('github', 'http://github.com/dmunguia'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/dmunguia/Documents/TEC/ic-itcr.ac.cr/pelican-bootstrap3"

STATIC_PATHS = [ 'static' ]

HIDE_SIDEBAR = True
CC_LICENSE = "CC-BY-NC"
ABOUT_ME = '''
Profesor de Ingeniería en Computación<br/>
TEC - Centro Académico de Alajuela<br/>
<strong>correo-e</strong>: <a href="mailto:dmunguia@itcr.ac.cr">dmunguia@itcr.ac.cr</a><br/>
<strong>twitter</strong>: <a href="http://twitter.com/diegomunguia">@diegomunguia</a><br/>
<strong>github</strong>: <a href="http://github.com/dmunguiatec">dmunguia</a><br/>
<a href="http://cr.linkedin.com/pub/diego-munguia/0/159/7a3"><img src="https://static.licdn.com/scds/common/u/img/webpromo/btn_profile_bluetxt_80x15.png" width="80" height="15" border="0" alt="View Diego Munguia's profile on LinkedIn"></a>
'''
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = None
