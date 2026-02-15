import os
from .base import *  # noqa

DEBUG = False

# 生产环境 allowed hosts（你原生产 settings）:contentReference[oaicite:22]{index=22}
ALLOWED_HOSTS = [
    "100.68.130.160",
    "127.0.0.1",
    "localhost",
]

# 生产环境数据库：MariaDB(MySQL backend)（你原生产 settings）:contentReference[oaicite:23]{index=23}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "blogdb"),
        "USER": os.getenv("DB_USER", "bloguser"),
        "PASSWORD": os.getenv("DB_PASSWORD", "147258"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    }
}

# 生产环境缓存：Redis（你原生产 settings）:contentReference[oaicite:24]{index=24}
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_URL", "redis://127.0.0.1:6379/1"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "TIMEOUT": 300,
    }
}

# Session 使用缓存（你原生产 settings）:contentReference[oaicite:25]{index=25}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 7 days
SESSION_SAVE_EVERY_REQUEST = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
