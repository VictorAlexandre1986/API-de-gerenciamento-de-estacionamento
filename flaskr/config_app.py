import os

DEFAULT_DATABASE = os.environ.get('DEFAULT_DATABASE', 'database.db')

DEFAULT_DATABASE_URL = os.environ.get(
    'DEFAULT_DATABASE_URL',
    f'sqlite:///{DEFAULT_DATABASE}'
)

SQLALCHEMY_TRACK_MODIFICATIONS = int(os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', '0')) == 1
SQLALCHEMY_ECHO = int(os.environ.get('SQLALCHEMY_ECHO', '0')) == 1

# SQLite doesn't support schema, so you can remove DEFAULT_DB_SCHEMA if it's not used elsewhere.

