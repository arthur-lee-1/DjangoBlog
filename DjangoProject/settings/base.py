"""
Base settings shared by all environments.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Security
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-4kob7aonafuc65wryo-y&%-&n@grko*7xn50!7t=@bsmct8ssg",  # 你当前文件里的值:contentReference[oaicite:4]{index=4}
)

# Default: let env files decide
DEBUG = False

# Default empty; env files override
ALLOWED_HOSTS: list[str] = []

# Application definition (沿用你当前配置):contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
    "accounts.apps.AccountsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DjangoProject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # 你当前 templates 目录配置:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}
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

WSGI_APPLICATION = "DjangoProject.wsgi.application"

# Database: must be defined in dev.py / prod.py
DATABASES: dict = {}

# Password validation (沿用你当前配置):contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization (沿用你当前配置):contentReference[oaicite:11]{index=11}:contentReference[oaicite:12]{index=12}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_TZ = True

# Static files (沿用你当前 STATIC_URL):contentReference[oaicite:13]{index=13}:contentReference[oaicite:14]{index=14}
STATIC_URL = "static/"

# Media (沿用你当前配置):contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16}
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 登录/登出 (沿用你当前配置):contentReference[oaicite:17]{index=17}:contentReference[oaicite:18]{index=18}
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Cache: env files decide (开发不用 Redis；生产用 Redis):contentReference[oaicite:19]{index=19}:contentReference[oaicite:20]{index=20}
CACHES: dict = {
    "default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}
}
