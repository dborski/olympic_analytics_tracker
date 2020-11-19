from .base import *
import os
# import psycopg2
import dj_database_url
import django_heroku

DEBUG = False

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'USER': os.getenv("USER"),
#         'PASSWORD': os.getenv("PASSWORD"),
#         'NAME': os.getenv("NAME"),
#         'HOST': os.getenv("HOST"),
#         'PORT': '5432',
#     }
# }

# DATABASE_URL = os.getenv('DATABASE_URL')

django_heroku.settings(locals())

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# DATABASES['default'] = dj_database_url.config(
#     conn_max_age=600, ssl_require=True)
DATABASES = {
    'default': dj_database_url.config(ssl_require=True)
}
