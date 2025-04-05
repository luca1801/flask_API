# isort: skip_file
"""
Flask API module.
"""

from flask import Flask

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from .extensions import db, api, marsh, migrate
from .views.employer_views import EmployerList
from .views import init_api

# from flask_restful import Api
# from flask_marshmallow import Marshmallow

# flask_api = Flask(__name__)
# flask_api.config.from_object('config')  # Load configuration from config.py

# api = Api(flask_api)
# db = SQLAlchemy(flask_api)
# marsh = Marshmallow(flask_api)
# migrate = Migrate(flask_api, db)

# from .views import employers_views
# from .models import employer_model

# api = Api()
# db = SQLAlchemy()
# marsh = Marshmallow()
# migrate = Migrate()


def create_app(config_name):
    """
    Create a Flask application using the app factory pattern.
    """
    app = Flask(__name__)

    # Load Config
    from config import config

    app.config.from_object(config[config_name])
    print(config_name)
    # app.config['ERROR_404_HELP'] = False

    db.init_app(app)
    marsh.init_app(app)
    if config_name != 'testing':
        migrate.init_app(app, db)
        print('migrate started')
    api.init_app(app)

    # Register API views(resources)
    init_api(api)

    # from .models import employer_model

    # api.add_resource(EmployerList, '/')

    with app.app_context():
        # api.add_resource(EmployerList, '/')
        # init_api(api)
        db.create_all()

    # from .models import employer_model
    # from .views import employer_views
    # from .schemas import employer_schema

    # shell context for flask cli
    # @app.shell_context_processor
    # def ctx():
    #     return {"app": app, "db": db, "api": api}

    return app


# class create_app():
#     def __init__(self, config_name='Config'):
#         self.app = Flask(__name__)
#         self.config_name = config_name
#         self.api = Api()
#         self.db = SQLAlchemy()
#         self.marsh = Marshmallow()
#         self.migrate = Migrate()
#         self.initialize()

#     def initialize(self):
#         self.app.config.from_object(self.config_name)
#         self.api.init_app(self.app)
#         self.db.init_app(self.app)
#         self.marsh.init_app(self.app)
#         self.migrate.init_app(self.app, self.db)

#         with self.app.app_context():
#             from .views import employers_views

#             from .models import employer_model

#         #from .models import employer_test
#         self.db.create_all()
#         return self.app

# app = create_app('config')
