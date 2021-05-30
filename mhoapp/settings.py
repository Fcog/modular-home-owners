"""
Django settings for mhoapp project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key
from django.urls import reverse_lazy
from machina import MACHINA_MAIN_TEMPLATE_DIR
from machina import MACHINA_MAIN_STATIC_DIR


load_dotenv()  # take environment variables from .env

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', get_random_secret_key())
WAGTAIL_SITE_NAME = 'Modular Home Owners'
MACHINA_FORUM_NAME = 'Modular Home Owners Forum'
TAILWIND_APP_NAME = 'mhoapp.theme'


# Development mode settings
# ------------------------------------------------------------------------------
DEBUG = os.getenv('DEBUG', 'False') == 'True'
DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE', 'False') == 'True'
DEBUG_BAR = False

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# ------------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,0.0.0.0,localhost').split(',')


# Application definition
# ------------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'wagtail_multi_image_edit', # This one should be installed before 'wagtail.admin'

    'wagtail.contrib.modeladmin',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.styleguide',
    'wagtail.contrib.settings',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
    'wagtailsvg', 
    'svg', # django-inline-svg
    'wagtail_link_block',
    'hitcount',
    'wagtailyoast',
    'wagtailcolumnblocks',
    'wagtail_multi_upload',
    'spurl', # https://github.com/j4mie/django-spurl

    # Machina dependencies:
    'mptt',
    'haystack',
    'widget_tweaks',

    # Machina apps:
    'machina',
    'machina.apps.forum',
    'machina.apps.forum_conversation',
    'machina.apps.forum_conversation.forum_attachments',
    'machina.apps.forum_conversation.forum_polls',
    'machina.apps.forum_feeds',
    'machina.apps.forum_moderation',
    'machina.apps.forum_search',
    'machina.apps.forum_tracking',
    'machina.apps.forum_member',
    'machina.apps.forum_permission',

    'storages',  # S3 buckets storage.
    'tailwind',
    'wagtailmenus',

    'mhoapp.authentication',
    'mhoapp.base',
    'mhoapp.homes',
    'mhoapp.partners',
    'mhoapp.articles',
    'mhoapp.flexible',
    'mhoapp.resources',
    'mhoapp.theme',
    'mhoapp.simplepage',
]

# Include apps only in dev env.
if DEVELOPMENT_MODE is True:
    INSTALLED_APPS += [
        'pattern_library', # Live styleguide
    ]

if DEVELOPMENT_MODE is True & DEBUG_BAR is True:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]


# Middleware
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
    "django_htmx.middleware.HtmxMiddleware"
]

# Include middleware only in dev env.
if DEVELOPMENT_MODE is True & DEBUG_BAR is True:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'mhoapp.urls'


# Templates
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'mhoapp/theme/templates',
            MACHINA_MAIN_TEMPLATE_DIR,
            'wagtail_multi_image_edit/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtailmenus.context_processors.wagtailmenus',
                'machina.core.context_processors.metadata',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'builtins': [
                'pattern_library.loader_tags'
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'mhoapp.wsgi.application'


# UI Pattern Library settings
# ------------------------------------------------------------------------------
PATTERN_LIBRARY = {
    # Groups of templates for the pattern library navigation. The keys
    # are the group titles and the values are lists of template name prefixes that will
    # be searched to populate the groups.
    'SECTIONS': (
        ('atoms', ['patterns/atoms']),
        ('molecules', ['patterns/molecules']),
        ('organisms', ['patterns/organisms']),
        ('templates', ['patterns/templates']),
        ('pages', ['patterns/pages']),
    ),

    # Configure which files to detect as templates.
    'TEMPLATE_SUFFIX': '.html',

    # Set which template components should be rendered inside of,
    # so they may use page-level component dependencies like CSS.
    'PATTERN_BASE_TEMPLATE_NAME': 'base.html',

    # Any template in BASE_TEMPLATE_NAMES or any template that extends a template in
    # BASE_TEMPLATE_NAMES is a "page" and will be rendered as-is without being wrapped.
    'BASE_TEMPLATE_NAMES': ['base_page.html'],
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------
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


# AUTH CONFIGURATION
# ------------------------------------------------------------------------------
LOGIN_URL = reverse_lazy('login')


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
WY_LOCALE = 'en_US'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# ------------------------------------------------------------------------------
if DEVELOPMENT_MODE is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }

else:
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# ------------------------------------------------------------------------------
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'mhoapp/theme/static'),
    MACHINA_MAIN_STATIC_DIR,
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SVG_DIRS = [
    os.path.join(BASE_DIR, 'media/media'),
    os.path.join(BASE_DIR, 'mhoapp/theme/static/svg'),
]

if DEVELOPMENT_MODE is True:
    # local storage
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
else:
    # Use AWS S3 storage
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_ENDPOINT_URL = os.environ['AWS_S3_ENDPOINT_URL']
    AWS_DEFAULT_ACL = 'public-read'

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    STATICFILES_LOCATION = 'static'
    MEDIAFILES_LOCATION = 'media'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

    STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_ENDPOINT_URL}/{MEDIAFILES_LOCATION}/'

# https://docs.wagtail.io/en/stable/reference/settings.html#usage-for-images-documents-and-snippets
WAGTAIL_USAGE_COUNT_ENABLED = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    },
}


# Search engine for the forum
# ------------------------------------------------------------------------------
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


# Debug toolbar config
# ------------------------------------------------------------------------------
INTERNAL_IPS = [
    '127.0.0.1',
    '172.22.0.1',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    # Toolbar options
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    # Panel options
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds
    'INTERCEPT_REDIRECTS': False,
}

# Multi image edit library config
# https://pypi.org/project/Wagtail-Multi-Image-Edit/
# ------------------------------------------------------------------------------
MULTI_IMAGE_EDIT_FIELDS = [
    'title',
    'collection',
]