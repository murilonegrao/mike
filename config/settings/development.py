"""
Django development settings for core project.

Extends base settings with development-specific configuration.
"""

from .base import *  # noqa: F401, F403


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-dev-key-change-me-in-production",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB', default='mike_db'),
        'USER': env('POSTGRES_USER', default='mike_user'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='mike_password'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('POSTGRES_PORT', default='5432'),
    }
}


# Email backend — console output for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
