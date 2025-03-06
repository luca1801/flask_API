# isort: skip_file
"""
Flask API module.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

flask_api = Flask(__name__)
flask_api.config.from_object('config')  # Load configuration from config.py

api = Api(flask_api)
db = SQLAlchemy(flask_api)
migrate = Migrate(flask_api, db)

from .views import employers_views
from .models import employer_model
