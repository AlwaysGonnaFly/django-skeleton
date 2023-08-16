from core.settings import BASE_DIR, config

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': config('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': config('DB_USER', 'user'),
        'PASSWORD': config('DB_PASSWORD', 'password'),
        'HOST': config('DB_HOST', 'localhost'),
        'PORT': config('DB_POST', '5432'),
    }
}
