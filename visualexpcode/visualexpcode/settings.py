# -*- coding: utf-8 -*-
"""
Django settings for visualexpcode project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*dfvt&cx8k%f)ydm3kfr=-(3+@6chowtj@p*1d=9=5v4kv-a*o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #AdminTools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    #core django modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #External Dependencies
    'polymorphic',
    'pipeline',
    'twitter_bootstrap',
    'jquery',
    'parler',
    'tinymce',
    'qrcode',
    #VisualexpModules
    'visualAdmin',#.apps.VisualadminConfig',
    'visualexpcode',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'visualexpcode.middleware.languages.language_cookie.LanguageCookieMiddleware',
    'visualexpcode.middleware.languages.language_cookie.AdminLocaleURLMiddleware',
]

ROOT_URLCONF = 'visualexpcode.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.core.context_processors.i18n',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

WSGI_APPLICATION = 'visualexpcode.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'visualexp',
        'USER': 'django',
        'PASSWORD' : 'django',
        'HOST' : '127.0.0.1',
        'PORT' : '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# FOR TESTING PURPOSES ! 
# Uncomment the display language 
LANGUAGE_CODE = 'fr' #Francais
#LANGUAGE_CODE = 'en' #Anglais
# LANGUAGE_CODE = 'de' #Allemand
#LANGUAGE_CODE = 'ru' #Russe
#LANGUAGE_CODE = 'zh-hans' #Chinois(Simplifie)


TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('fr', _('Français')),
    ('en', _('Anglais')),
    ('de', _('Allemand')),
    ('ru', _('Russe')),
    ('zh-hans', _('Chinois (Simplifié)')),
    ('zh-hant', _('Chinois (Traditionnel)'))
]

# @TODO Add missing langs
PARLER_LANGUAGES = {
    None: (
        {'code': 'fr',},
        {'code': 'en',},
        {'code': 'de',},
        {'code': 'ru',},
        {'code': 'zh-hans',},
        {'code': 'zh-hant'},
    ),
    'default': {
        'fallbacks': ['fr'],          # defaults to PARLER_DEFAULT_LANGUAGE_CODE
        'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
    }
}

ADMIN_LANGUAGE_CODE='fr'


LOCALE_PATHS = (
    '/var/visualexp/locale',
)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# Use pipeline to create and serve asset groups
# http://django-pipeline.readthedocs.io/en/latest/index.html

STATIC_URL = '/static/'
STATIC_ROOT = '/var/visualexp/static'
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

#Get bootstrap less files
#For our less files
#my_app_less = os.path.join(BASE_DIR, 'my_app', 'static', 'less')
visualexp_less = os.path.join(BASE_DIR, 'visualexpcode', 'static', 'less')

# For apps outside of your project, it's simpler to import them to find their root folders
import twitter_bootstrap
bootstrap_less = os.path.join(os.path.dirname(twitter_bootstrap.__file__), 'static', 'less')

#PIPELINE_LESS_ARGUMENTS = u'--include-path={}'.format(os.pathsep.join([bootstrap_less, my_app_less]))


PIPELINE = {
# Compress assets, defaults to not settings.DEBUG 
# enable for production 
#   'PIPELINE_ENABLED': True,
    'COMPILERS': {
        'pipeline.compilers.less.LessCompiler',
    },
    'LESS_BINARY': {
        '/usr/local/bin/lessc',
    },
    'LESS_ARGUMENTS': {
        u'--include-path={}'.
        format(os.pathsep.join([bootstrap_less, visualexp_less])),
    },
    'YUGLIFY_BINARY': {
        '/usr/local/bin/yuglify',
    },
    'STYLESHEETS': {
        'bootstrap': {
            'source_filenames': (
                'twitter_bootstrap/less/bootstrap.less',
            ),
            'output_filename': 'css/b.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
        'default': {
            'source_filenames': (
                'less/default.less',
            ),
            'output_filename': 'css/default.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
        'imageMap': {
            'source_filenames': (
                'imageMap/imagemap.less',
            ),
            'output_filename': 'css/imagemap.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'bootstrap': {
            'source_filenames': (
              'js/jquery.js',
              'twitter_bootstrap/js/transition.js',
              'twitter_bootstrap/js/modal.js',
              'twitter_bootstrap/js/dropdown.js',
              'twitter_bootstrap/js/scrollspy.js',
              'twitter_bootstrap/js/tab.js',
              'twitter_bootstrap/js/tooltip.js',
              'twitter_bootstrap/js/popover.js',
              'twitter_bootstrap/js/alert.js',
              'twitter_bootstrap/js/button.js',
              'twitter_bootstrap/js/collapse.js',
              'twitter_bootstrap/js/carousel.js',
              'twitter_bootstrap/js/affix.js',
              'js/js-cookie.js',
            ),
        'output_filename': 'js/b.js',
        },
        'rwdImageMaps': {
            'source_filenames': (
                'rwdImageMaps/jquery.rwdImageMaps.min.js',
            ),
        'output_filename': 'js/rwdImageMaps.min.js',
        },
    },
}

# User Uploaded Content ( For artworks )
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-MEDIA_ROOT
# https://docs.djangoproject.com/en/1.9/ref/models/fields/#filefield
MEDIA_ROOT = '/var/visualexp/media/'
MEDIA_URL = '/media/'

ADMIN_TOOLS_INDEX_DASHBOARD = 'visualAdmin.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'visualAdmin.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_THEMING_CSS = 'css/theming.css'
