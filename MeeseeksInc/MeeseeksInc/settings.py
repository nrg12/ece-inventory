"""
Django settings for MeeseeksInc project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x6s74m_9(u*#)ntmwf0g&1xpwh^7#x4m$07-*xzq4=l^qg!rhw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['colab-sbx-48.oit.duke.edu', 'colab-sbx-248.oit.duke.edu','meeseeksinc.colab.duke.edu', '127.0.0.1','localhost','colab-sbx-134.oit.duke.edu', 'meeseeks.colab.duke.edu','152.3.53.138']

# Application definition

INSTALLED_APPS = [
#     'admin_tools',
#     'admin_tools.theming',
#     'admin_tools.menu',
#     'admin_tools.dashboard',
#     'bootstrap3',
    'custom_admin.tasks',
    'dal',
    'dal_select2',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    'custom_admin.apps.CustomAdminConfig',
    'inventory.apps.InventoryConfig', # added this so Django knows about the app 'inventory'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MeeseeksInc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
#         'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                ]),
            ]
        },
        
    },
]

WSGI_APPLICATION = 'MeeseeksInc.wsgi.application'

DATABASES = {

    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'meeseeksadmin',
	'USER': 'admin',
	'PASSWORD':'admin', 
	'HOST':'localhost', 
	'PORT':'5432',
    }

}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern' # change this since we are in EST
USE_TZ = True
USE_I18N = True

USE_L10N = True


GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
'''

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# EMAIL
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'nrg12'
EMAIL_HOST_PASSWORD = 'meeseeksinc1'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# CELERY
BROKER_URL = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZEr = 'json'


#This did the trick
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


ADMIN_TOOLS_MENU = 'MeeseeksInc.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'MeeseeksInc.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'MeeseeksInc.dashboard.CustomAppIndexDashboard'