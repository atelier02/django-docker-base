from main.base_settings import *
import os
import dj_database_url
from decouple import config, Csv
import django_heroku


# settings for production(heroku)
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {  # 'catch all' loggers by referencing it with the empty string
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

# DB configuration
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=["*"], cast=Csv())


# Activate Django-Heroku.
django_heroku.settings(locals())
