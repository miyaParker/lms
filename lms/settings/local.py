from .base import *
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'news',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}