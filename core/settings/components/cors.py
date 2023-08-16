from corsheaders.defaults import default_methods, default_headers

from core.settings import config

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', '').split()
CORS_ALLOW_ALL_ORIGINS = bool(int(config('CORS_ALLOW_ALL_ORIGINS', '1')))
CORS_PREFLIGHT_MAX_AGE = 86400  # day
CORS_ALLOW_METHODS = (
    *default_methods,
)
CORS_ALLOW_HEADERS = (
    *default_headers,
)

# CORS_URLS_REGEX=
