# djangodocker/settings/development.py
from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY", "developmentKeyIsEmpty")
DEBUG = True

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB', 'leaveManagementSystem'),
        'USER': os.environ.get('POSTGRES_USER', 'lms'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'lms@123'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}

# print sql to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    },
}

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]
