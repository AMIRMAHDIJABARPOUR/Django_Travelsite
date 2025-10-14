from .base import *
from decouple import config

# تنظیمات امنیتی برای تولید
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['travelsite.liara.run', 'www.travelsite.liara.run']  # بعداً به ['yourdomain.com', 'www.yourdomain.com'] تغییر دهید

# دیتابیس تولید (PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config('DB_NAME'),
        "USER": config('DB_USER'),
        "PASSWORD": config('DB_PASSWORD'),
        "HOST": config('DB_HOST', default='db.liara.ir'),
        "PORT": config('DB_PORT', default='5432'),
    }
}

# تنظیمات فایل‌های استاتیک و مدیا برای لیارا
STATIC_URL = '/static/'
STATIC_ROOT = '/app/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/app/media/'
STATICFILES_DIRS = []

# تنظیمات امنیتی HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# تنظیمات ایمیل
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')

# تنظیمات کپچا
MULTI_CAPTCHA_ADMIN = {
    "engine": "simple-captcha",
}
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]