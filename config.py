# DEBUG = True

# USERNAME = 'kiki'
# PASSWORD = 'kiki'
# SERVER = 'localhost'
# DB = 'flask_api'

# SQLALCHEMY_DATABASE_URI = (
#     f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
# )
# SQLALCHEMY_TRACK_MODIFICATIONS = True

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    CONNECTION_FACTORY = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_TEST')


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'default': DevelopmentConfig,
}
