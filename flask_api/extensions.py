from flask_marshmallow import Marshmallow

# from flask_restful import Api
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate


db = SQLAlchemy()
api = Api(
    title='Employer Management API',
    version='1.0',
    description='API for employer registration and management',
    doc='/docs',
)
marsh = Marshmallow()
migrate = Migrate()
