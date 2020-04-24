from .base import *

DEBUG = False

ALLOWED_HOSTS = os.environ.setdefault('WAGTAILWEBSITEBUILDER_ALLOWED_HOST', '')
ALLOWED_HOSTS = ALLOWED_HOSTS.split(',')

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.setdefault(
            'WAGTAILWEBSITEBUILDER_DATABASE_NAME', ''),
        'USER': os.environ.setdefault('WAGTAILWEBSITEBUILDER_USER', ''),
        'PASSWORD': os.environ.setdefault(
            'WAGTAILWEBSITEBUILDER_DATABASE_PASSWORD',
            ''),
        'HOST': os.environ.setdefault(
            'WAGTAILWEBSITEBUILDER_DATABASE_HOST', ''),
        'PORT': os.environ.setdefault(
            'WAGTAILWEBSITEBUILDER_DATABASE_PORT', ''),
    }
}

MEDIA_ROOT = os.environ.setdefault(
    'WAGTAILWEBSITEBUILDER_MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))
MEDIA_URL = os.environ.setdefault('WAGTAILWEBSITEBUILDER_MEDIA_URL', '/media/')

COMPRESS_OFFLINE = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
