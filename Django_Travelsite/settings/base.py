import os
from pathlib import Path
import mimetypes

from django.conf.global_settings import STATIC_ROOT

# مسیر ریشه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# اپلیکیشن‌های نصب‌شده
INSTALLED_APPS = [
    "multi_captcha_admin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django_extensions",
    "robots",
    "captcha",
    "taggit",
    "home_page.apps.HomePageConfig",
    "blog_page.apps.BlogPageConfig",
]

# میدلورها
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# تنظیمات URL
ROOT_URLCONF = "Django_Travelsite.urls"

# تنظیمات قالب‌ها
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# تنظیمات WSGI
WSGI_APPLICATION = "Django_Travelsite.wsgi.application"

# تنظیمات پیش‌فرض برای فیلدهای Auto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# تنظیمات فایل‌های استاتیک و مدیا
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# تنظیمات robots.txt
ROBOTS_USE_HOST = False
ROBOTS_USE_SITEMAP = True


# تنظیمات چندزبانه
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# تنظیمات لاگین
LOGIN_URL = 'accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# تنظیمات MIME برای جاوااسکریپت
mimetypes.add_type("application/javascript", ".js", True)

# تنظیمات سایت
SITE_ID = 2