from main.base_settings import *
import pymysql
import dj_database_url
from decouple import config, Csv


# settings for development
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
            'level': 'DEBUG',
        },
    },
}

# DB configuration
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default="sqlite:///db.sqlite3")
    )
}

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=["*"], cast=Csv())