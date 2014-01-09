# -*- coding: utf-8 -*-
# Django settings for tuto_sdz project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
(u'Cyril Mizzi', 'cyril.mizzi@gmail.com'),
(u'Natim', 'natim@siteduzero.com'),
(u'Cam', 'cam@siteduzero.com')
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2','postgresql', 'mysql', 'sqlite3' or 'oracle'.
'NAME': 'tuto_sdz.db', # Or path to database file if using sqlite3.
'USER': '', # Not used with sqlite3.
'PASSWORD': '', # Not used with sqlite3.
'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
'PORT': '', # Set to empty string for default. Not used with sqlite3.
}
}

# Vous pouvez trouver la liste complète ici :
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# Tous les choix ne sont peut-être pas disponibles sur votre OS.
# Sous Windows, ce doit être le même que le système.
TIME_ZONE = 'Europe/Paris'
# Code de la langue de votre installation. Liste complète ici :
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-fr'
SITE_ID = 1
# Votre projet est-il prévu pour être multilingue ? Sous Django,
# il vaut mieux coder systématiquement pour le multilingue.
# Cela ne coûte pas grand-chose et simplifie la vie par la suite.
USE_I18N = True
# Chemin absolu vers les fichiers statiques CSS, IMG, ...
# Exemple : "/home/media/media.lawrence.com/"
MEDIA_ROOT = 'C:/tuto_sdz/medias/'
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/medias/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'
# Elle doit être unique et n'être partagée avec personne.
SECRET_KEY = '$)0pbx@_v+&qg+=__tv7bj+ct*90w2#p#fvoy%iui-_rxlkae0'
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
'django.middleware.common.CommonMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = 'tuto_sdz.urls'
TEMPLATE_DIRS = ['C:/tuto_sdz/templates']

INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'sondages',
# Uncomment the next line to enable the admin:
 'django.contrib.admin',
)
























"""
Django settings for tuto_sdz project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

### Build paths inside the project like this: os.path.join(BASE_DIR, ...)
##import os
##BASE_DIR = os.path.dirname(os.path.dirname(__file__))
##
##
### Quick-start development settings - unsuitable for production
### See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
##
### SECURITY WARNING: keep the secret key used in production secret!
##SECRET_KEY = '$)0pbx@_v+&qg+=__tv7bj+ct*90w2#p#fvoy%iui-_rxlkae0'
##
### SECURITY WARNING: don't run with debug turned on in production!
##DEBUG = True
##
##TEMPLATE_DEBUG = True
##
##ALLOWED_HOSTS = []
##
##
### Application definition
##
##INSTALLED_APPS = (
##    'django.contrib.admin',
##    'django.contrib.auth',
##    'django.contrib.contenttypes',
##    'django.contrib.sessions',
##    'django.contrib.messages',
##    'django.contrib.staticfiles',
##)
##
##MIDDLEWARE_CLASSES = (
##    'django.contrib.sessions.middleware.SessionMiddleware',
##    'django.middleware.common.CommonMiddleware',
##    'django.middleware.csrf.CsrfViewMiddleware',
##    'django.contrib.auth.middleware.AuthenticationMiddleware',
##    'django.contrib.messages.middleware.MessageMiddleware',
##    'django.middleware.clickjacking.XFrameOptionsMiddleware',
##)
##
##ROOT_URLCONF = 'tuto_sdz.urls'
##
##WSGI_APPLICATION = 'tuto_sdz.wsgi.application'
##
##
### Database
### https://docs.djangoproject.com/en/dev/ref/settings/#databases
##
##DATABASES = {
##    'default': {
##        'ENGINE': 'django.db.backends.sqlite3',
##        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
##    }
##}
##
### Internationalization
### https://docs.djangoproject.com/en/dev/topics/i18n/
##
##LANGUAGE_CODE = 'en-us'
##
##TIME_ZONE = 'UTC'
##
##USE_I18N = True
##
##USE_L10N = True
##
##USE_TZ = True
##
##
### Static files (CSS, JavaScript, Images)
### https://docs.djangoproject.com/en/dev/howto/static-files/
##
##STATIC_URL = '/static/'
