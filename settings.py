
##################################################################
# Changing settings here is not recomended!!
#
# You can provide setting overrides in one of the provided settings 
# file in config/settings. Or you can create your own using one of 
# those files as starting point.
#
# Django will check for the value of DJANGO_ENV[_<project_name>][_<site_id>]
# to choose which setting to load at runtime. 
#
# default.py will always be used as fallback override
#
###################################################################

import os
import sys
PROJECT_ROOT = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename(PROJECT_ROOT)
# Django settings for javara project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i@8m%wswq$u(r($hmad#c1(e%$gsupj)t6p+-e7m1y^w$tq#r1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'javara.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

###################################################################
import os
import sys
from django.core.exceptions import ImproperlyConfigured

# Add project specific 3rd party lib to PYTHONPATH
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'lib'))

#
# Load settings override based on DJANGO_ENV[_<proj_name>] 
#

# First asserts that default.py exists
try:
    assert os.path.exists(os.path.join('config','settings','default.py'))
except AssertionError:
    raise ImproperlyConfigured("Something wen't very wrong. There should be a config/settings/default.py")

# Use 'default' as fallback 
settings_name = 'default'

# Probe DJANGO_ENV then DJANGO_ENV_<PROJECT_NAME> for settings override name
if os.environ.get('DJANGO_ENV', False):
    settings_name = os.environ.get('DJANGO_ENV', False)
elif os.environ.get('%s_ENV' % (PROJECT_NAME.upper()), False):
    settings_name =  os.environ.get('%s_ENV' % (PROJECT_NAME.upper()), False)

# Finally, load settings override
try:
    exec 'from config.settings.%s import *' % (settings_name)
except ImportError, e:
    raise ImproperlyConfigured(u'%s'% e.message)
