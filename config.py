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


# class Config:
#     if os.getenv('FLASK_CONFIG') == 'development':
#         # os.environ['FLASK_CONFIG'] = 'development'
#         SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_DATABASE_DEVELOPMENT')
#     elif os.getenv('FLASK_CONFIG') == 'testing':
#         SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_DATABASE_TESTING')
#     else:
#         raise ValueError(
#             "FLASK_CONFIG must be either 'development' or 'testing'"
#         )
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
#     # DEBUG = False
#     # TESTING = False
#     # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class DevelopmentConfig:
    # os.environ['FLASK_CONFIG'] = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_DATABASE_DEVELOPMENT')
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class TestConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    # os.environ['FLASK_CONFIG'] = 'testing'
    # os.putenv('FLASK_CONFIG', 'testing')
    # DEBUG = True
    # os.environ['FLASK_CONFIG'] = 'testing'
    # DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('FLASK_DATABASE_TEST')


config = {'development': DevelopmentConfig, 'testing': TestConfig}

print(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
print(TestConfig.SQLALCHEMY_DATABASE_URI)
