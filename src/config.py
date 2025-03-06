DEBUG = True

USERNAME = 'kiki'
PASSWORD = 'kiki'
SERVER = 'localhost'
DB = 'flask_api'

SQLALCHEMY_DATABASE_URI = (
    f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
)
SQLALCHEMY_TRACK_MODIFICATIONS = True
