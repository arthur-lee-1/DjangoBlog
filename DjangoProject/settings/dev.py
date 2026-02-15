from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# 开发环境数据库：sqlite3（你原开发 settings）:contentReference[oaicite:21]{index=21}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 开发环境：不配置 Redis（你说的“没有配置缓存”）
# 但为了避免某些地方调用 cache 报错，给一个本地内存缓存（足够轻量）
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}
