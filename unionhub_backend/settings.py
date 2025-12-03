"""
Django settings for unionhub_backend project.
"""

import os
from pathlib import Path

# -----------------------------------------
# BASE DIRECTORY
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------
# SECURITY
# -----------------------------------------
SECRET_KEY = 'django-insecure-j*v8gtv-^bl+_r3c$2q5vpk1dvzd1=fk%kr-h4(9gy&42j(ft_'

DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://csce-3444-union-hub-production.up.railway.app",
    "https://*.up.railway.app",
]

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# -----------------------------------------
# APPLICATIONS
# -----------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'formapp',
]

# -----------------------------------------
# MIDDLEWARE
# -----------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------------------
# URL CONFIG
# -----------------------------------------
ROOT_URLCONF = 'unionhub_backend.urls'

# -----------------------------------------
# TEMPLATES
# -----------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],   # Auto-detect app templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -----------------------------------------
# WSGI
# -----------------------------------------
WSGI_APPLICATION = 'unionhub_backend.wsgi.application'

# -----------------------------------------
# DATABASE
# -----------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------
# PASSWORD VALIDATION
# -----------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------
# INTERNATIONALIZATION
# -----------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------------------
# AUTO FIELD
# -----------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
