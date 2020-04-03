from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.setdefault('WAGTAILWEBSITEBUILDER_SECRET_KEY', '')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
