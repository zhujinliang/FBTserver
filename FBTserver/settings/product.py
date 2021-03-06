# -*- coding: utf-8 -*-

try:
    from FBTserver.settings.default import *
except ImportError:
    pass

ALIVE_ON_PRODUCTION = True
DEBUG = not ALIVE_ON_PRODUCTION
TEMPLATE_DEBUG = DEBUG

# Specify custom settings here.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'FBT',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


