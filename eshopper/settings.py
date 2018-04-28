"""
Django settings for eshopper project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '04kh!wy)e4i0mc3*xda7#jt9y6e@hy379g#)2cnsh93bqdy44&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1', ]


# Application definition

INSTALLED_APPS = (
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.sites',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'parler',
    'rosetta',
    'paypal.standard.ipn',
    'crispy_forms',
    'sorl.thumbnail',
    'newsletter',
    'tinymce',
    'django_extensions',

    # my apps
    'home',
    'about',
    'contact',
    'faq',
    'privacy-policy',
    'refund-policy',
    'onlineshop',
    'cart',
    'orders',
    'payment',
    'coupons',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'eshopper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'eshopper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eshopper',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': 5432

    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Africa/Accra'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('American English')),
    ('en-gb', _('British English')),
    ('es', _('Spanish')),
    ('zh-cn', _('Chinese')),
    ('pt', _('Portuguese')),
    ('ru', _('Russian')),
    ('nl', _('Dutch')),
    ('ko', _('Korean')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('he', _('Hebrew')),
    ('hi', _('Hindi')),
    ('fr', _('French')),
    ('de', _('German')),
    ('el', _('Greek')),
    ('ca', _('Catalan')),
    ('af', _('Afrikaans')),
    ('ar', _('Arabic')),
    ('tr', _('Turkish')),
    ('ga', _('Irish')),
    ('cy', _('Welsh')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static')
]

# Media Files ( User Media Uploads )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Key to store the cart in the user session.
CART_SESSION_ID = 'cart'

# django-paypal settings
PAYPAL_RECEIVER_EMAIL = 'daviose@mail.regent.edu'
PAYPAL_TEST = True


# Django Email configuration
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = ""
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
DEFAULT_FROM_EMAIL = 'E-Shopper <noreply@eshopper.com>'


# Redis settings
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

PARLER_LANGUAGES = {
        1: (
                {'code': 'en', },
                {'code': 'en-gb', },
                {'code': 'es', },
                {'code': 'zh-cn', },
                {'code': 'pt', },
                {'code': 'ru', },
                {'code': 'nl', },
                {'code': 'ko', },
                {'code': 'it', },
                {'code': 'ja', },
                {'code': 'he', },
                {'code': 'hi', },
                {'code': 'fr', },
                {'code': 'de', },
                {'code': 'el', },
                {'code': 'ca', },
                {'code': 'af', },
                {'code': 'ar', },
                {'code': 'tr', },
                {'code': 'ga', },
                {'code': 'cy', },
        ),
        'default': {
                    'fallback': 'en',
                    'hide_untranslated': False,
                }
}

JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

# Django - Jet theme colors for admin backend.
JET_DEFAULT_THEME = 'light-gray'

JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'   # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# Path to Google Analytics client_secrets.json
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(BASE_DIR, 'client_secrets.json')


# Registration App account settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[E-Shopper]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

# Sets the default site
SITE_ID = 1

# After successful login direct user to the profile page
LOGIN_REDIRECT_URL = '/profile'

# After successful logout direct user to the homepage
LOGOUT_REDIRECT_URL = '/'

# After successful registrations directs user to the profile homepage
SIGNUP_REDIRECT_URL = '/profile'

# Sets the default template pack for the project
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1

# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60

# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100

# Using django-tinymce
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"