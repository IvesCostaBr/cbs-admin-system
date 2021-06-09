from pathlib import Path
from decouple import config
import os
from django.apps import AppConfig

ADMINS = [('IvesCosta', 'ivescosta@cerberussistem.com.br')]

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['sistemarh.cerberussistem.com.br', '127.0.0.1', 'localhost', '172.31.63.255']

AppConfig.default = False #TODO:Setando default como False o django passa a aceitar apps vindo de diretorios diferente 
AppConfig.ignore_patterns = [''] 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',

    #myapps
    'apps.company',
    'apps.collaborator',
    'apps.departament',
    'apps.documents',
    'apps.register_extra_hour',
    'apps.core',
    'apps.task',
    'bootstrap4',
    'django_celery_results',
    'django_celery_beat',
    'corsheaders',
 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
  

]

ROOT_URLCONF = 'admin_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'admin_system.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'antigo': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

#TODO:Caso a empresa possuir um servidor de arquivo separado podemos simplesente colocar a url absoluta na viariavel MEDIA__ROOT
MEDIA_ROOT = 'media/'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = [
    BASE_DIR / "static",
    #'/var/www/static/',
]
LOGIN_URL = 'login'        
LOGIN_REDIRECT_URL = 'redirect'
LOGOUT_REDIRECT_URL = 'redirect'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = 1

CORS_ALLOWED_ORIGINS = [
  
    "http://localhost:4200",

]