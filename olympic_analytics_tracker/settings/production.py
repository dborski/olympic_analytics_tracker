from .base import *
import os
import dj_database_url
import django_heroku

DEBUG = False

django_heroku.settings(locals())

DATABASES = {
    'default': dj_database_url.config(ssl_require=True)
}
