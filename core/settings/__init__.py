from pathlib import Path
from decouple import AutoConfig

from split_settings.tools import include, optional

# direction with manage.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# load .env files
config = AutoConfig(search_path=BASE_DIR.joinpath('config'))

# base variables
SECRET_KEY = config('SECRET_KEY')
DEBUG = int(config('DEBUG', 1))
ALLOWED_HOSTS = config('ALLOWED_HOSTS', '*').split()
INTERNAL_IPS = config('INTERNAL_IPS', '').split()

# import setting components
base_settings = [
    'components/apps.py',
    'components/middleware.py',
    'components/database.py',
    'components/template.py',
    'components/cache.py',
    'components/logging.py',
    'components/other.py',
    'components/tz.py',

    # files
    'components/static.py',
    'components/media.py',

    # security
    'components/security.py',
    'components/cors.py',
    'components/defender.py',

    # dev/prod
    'production.py',
    optional('development.py')
]

include(*base_settings)
