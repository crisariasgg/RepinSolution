"""
Django settings for project.
"""

# Standard library
import environ
from pathlib import Path


env = environ.Env()
environ.Env.read_env()

# APPS DIR
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('apps')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print('VERIFIACAR EL BASE DIR',BASE_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DJANGO_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	

]
THIRD_PARTY_APPS = ['simple_history','import_export']
LOCAL_APPS = [
	'apps.users',
	'apps.import_excel', #Dashboard
	'apps.utils',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Third party middlewares
    'simple_history.middleware.HistoryRequestMiddleware',

]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [Path.joinpath(BASE_DIR,'templates')],
		
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ShopifyImport',
        'USER': 'root',
        'PASSWORD': 'Minimalista1',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	Path.joinpath(BASE_DIR,'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')

STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Admin
ADMIN_URL = 'admin/'
ADMINS = [
	("""Cristopher Arias""" , 'crisarias@grupoguticia.com')
]

# CACHES
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'LOCATION': '',
	}
}

AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/users/index'
LOGIN_URL = '/'
