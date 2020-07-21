import os
import dj_database_url

from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASE_URL = environ.get('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.config(os.environ.get('DATABASE_URL'))
}
