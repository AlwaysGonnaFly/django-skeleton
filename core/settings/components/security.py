from core.settings import config

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

X_FRAME_OPTIONS = 'DENY'

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = bool(int(config('SECURE_SSL_REDIRECT', '0')))
SECURE_BROWSER_XSS_FILTER = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_PATH = '/'
CSRF_COOKIE_SAMESITE = config('SESSION_CSRF_COOKIE_SAMESITE', 'Lax')
CSRF_COOKIE_AGE = 31449600
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'  # представление ошибки проверки csrf
CSRF_USE_SESSIONS = True

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_PATH = '/'
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_AGE = int(config('SESSION_COOKIE_AGE', 1209600))
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
