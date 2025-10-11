from .base import *
from decouple import config

DEBUG = True
SECRET_KEY = "django-insecure-i!j_u$cpfu(-rqfo%j$@b=8l+vm+pg5-ny(!%^950nle@upo9#"
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# دیتابیس PostgreSQL برای توسعه
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "OPTIONS": {
            "timeout": 60,  # ثانیه
        },
    }
}

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]

MULTI_CAPTCHA_ADMIN = {
    "engine": "simple-captcha",
}
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False