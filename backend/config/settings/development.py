"""Development settings."""
from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

# Dev-only middleware
if "debug_toolbar" not in MIDDLEWARE:
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INSTALLED_APPS += ["debug_toolbar"]

INTERNAL_IPS = ["127.0.0.1"]

# Console-friendly logging
LOGGING["root"]["level"] = "DEBUG"  # noqa

# Open CORS in dev
CORS_ALLOW_ALL_ORIGINS = True
