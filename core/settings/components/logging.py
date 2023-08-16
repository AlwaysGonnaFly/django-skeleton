from core.settings import BASE_DIR, config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] - %(levelname)s [%(name)s:%(lineno)s] | %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'db': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': BASE_DIR / 'logs/db.log',
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'backupCount': 5
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['db'],
            'level': config('LEVEL_DB_LOGS', 'DEBUG'),
        },
    },
}
