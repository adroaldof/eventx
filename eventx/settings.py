"""
Django settings for eventx project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Use python decouple
from decouple import config
# Use dj database
from dj_database_url import parse as db_url
# Use unipath do get
from unipath import Path
BASE_DIR = Path(__file__).parent

from django.utils.translation import ugettext as _


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.herokuapp.com']


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THYRD_PARTY_APPS = (
    'south',
)

LOCAL_APPS = (
    'core',
    'subscriptions',
    'accounts',
)

INSTALLED_APPS = DJANGO_APPS + THYRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'eventx.urls'

WSGI_APPLICATION = 'eventx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

# Languages available on this system.
LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _('Portuguese')),
)

print BASE_DIR.ancestor(1).child('locale') + '/'
LOCALE_PATHS = (
    BASE_DIR.ancestor(1).child('locale') + '/',
)

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

# Use South to manage data base on tests?
# True: Yes. (default)
# False: No! Use SyncDB
# SOUTH_TESTS_MIGRATE = False


# Change default user auth
AUTH_USER_MODEL = 'accounts.User'


# Chage authentication backends
# AUTHENTICATION_BACKENDS = (
#     'accounts.backends.EmailBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )
