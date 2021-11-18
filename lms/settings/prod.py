from .base import *
DEBUG = False

ALLOWED_HOSTS = ['api.kodecamp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_db',
        'HOST': 'prod_host',
        'PORT': '5432',
    }
}