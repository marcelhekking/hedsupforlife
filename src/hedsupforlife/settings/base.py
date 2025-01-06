"""
Django settings for hedsupforlife Website.

"""

import os
from pathlib import Path

from django.urls import reverse_lazy

# Automatically figure out the ROOT_DIR and PROJECT_DIR.
path = Path(__file__)

DJANGO_PROJECT_DIR = path.parent.parent
SRC_DIR = DJANGO_PROJECT_DIR.parent
ROOT_DIR = DJANGO_PROJECT_DIR.parent.parent


ADMINS = [
    ("marcel", "marcelhekking@gmail.com"),
]

SECRET_KEY = os.getenv("SECRET_KEY", "a key")

SITE_ID = 1

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

DEBUG = os.getenv("DEBUG", False)

# Application definition

INSTALLED_APPS = [
    # project apps...
    "hedsupforlife",
    "hedsupforlife.home",
    # wagtail apps...
    "wagtail.locales",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.contrib.modeladmin",
    "wagtail",
    "wagtailfontawesomesvg",
    "modelcluster",
    "taggit",
    # django apps...
    "django_browser_reload",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
]

MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hedsupforlife.urls"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.DefaultStorageFinder",
]

STATICFILES_DIRS = (str(SRC_DIR / "static"),)

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = str(ROOT_DIR / "/local/staticfiles")
MEDIA_ROOT = str(ROOT_DIR / "local/mediafiles")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(SRC_DIR / "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.static",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "hedsupforlife.wsgi.application"

FIXTURE_DIRS = Path(ROOT_DIR) / "tests"

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/


TIME_ZONE = "Europe/Amsterdam"
USE_I18N = True

LANGUAGE_CODE = "nl"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("nl", "Dutch"),
    ("en", "English"),
]

LOCALE_PATHS = (str(SRC_DIR / "locale"),)


# EMAIL
EMAIL_HOST = "smtp.hostnet.nl"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "test@fastmail.nl")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "a secret")
EMAIL_RECIPIENT_LIST = os.getenv("EMAIL_RECIPIENT_LIST", "one,two").split(",")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "test@fastmail.nl")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = reverse_lazy("auth_login")

# Wagtail
WAGTAIL_SITE_NAME = "hedsupforlife"
# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "https://hedsupforlife.nl/"
