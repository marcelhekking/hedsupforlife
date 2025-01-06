import os  # noqa
from .base import *  # noqa
import environ

DJANGO_SETTINGS_MODULE = "hedsupforlife.settings.develop"
DEBUG = True
env = environ.Env()


DATABASES = {"default": env.db(default="postgresql://localhost/hedsupforlife")}


LOGGING = {  # noqa
    "version": 1,
    "disable_existing_loggers": False,
    "django": {
        "handlers": ["django"],
        "level": "INFO",
        "propagate": True,
    },
}
