import os  # noqa

from .base import *  # noqa
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("SQL_DATABASE", "database"),
        "USER": os.getenv("SQL_USER", "user"),
        "PASSWORD": os.getenv("SQL_PASSWORD", "password"),
        "HOST": os.getenv("SQL_HOST", "localhost"),
        "PORT": os.getenv("SQL_PORT", "5432"),
    }
}

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    "localhost",
    "hedsupforlife",
    "hedsupforlife.nl",
    "www.hedsupforlife.nl",
    "64.225.64.24",
]

STATIC_ROOT = "../public/staticfiles/"

MEDIA_ROOT = "../public/mediafiles/"

LOGGING = {  # noqa
    "version": 1,
    "disable_existing_loggers": False,
    "django": {
        "handlers": ["django"],
        "level": "INFO",
        "propagate": True,
    },
}

CSRF_TRUSTED_ORIGINS = ["https://hedsupforlife.nl"]


# SENTRY
sentry_sdk.init(
    dsn="https://d0b39fc268e24d669c5e3b41e750a94a@app.glitchtip.com/7861",
    integrations=[DjangoIntegration()],
    auto_session_tracking=False,
    traces_sample_rate=0,
)
