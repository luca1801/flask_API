# isort: skip_file
"""
Flask API module.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow

# flask_api = Flask(__name__)
# flask_api.config.from_object('config')  # Load configuration from config.py

# api = Api(flask_api)
# db = SQLAlchemy(flask_api)
# migrate = Migrate(flask_api, db)

# from .views import employers_views
# from .models import employer_model

api = Api()
db = SQLAlchemy()
marsh = Marshmallow()
migrate = Migrate()


def create_app(config_name='config'):
    """
    Create a Flask application using the app factory pattern.
    """
    app = Flask(__name__)
    app.config.from_object(config_name)
    api.init_app(app)
    db.init_app(app)
    marsh.init_app(app)

    migrate.init_app(app, db)

    with app.app_context():
        from .views import employers_views

        from .models import employer_model

        # from .models import employer_test

        db.create_all()
    return app
