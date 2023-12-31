# Cache (django-cachalot)
# https://django-cachalot.readthedocs.io/en/latest/

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0'
    }
}

CACHALOT_ENABLED = True
CACHALOT_CACHE = 'default'
CACHALOT_TIMEOUT = None
CACHALOT_INVALIDATE_RAW = True
