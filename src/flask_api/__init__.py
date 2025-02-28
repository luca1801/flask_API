# isort: skip_file
"""
Flask API module.
"""

from flask import Flask

from flask_restful import Api

flask_api = Flask(__name__)
flask_api.config.from_object('config')  # Load configuration from config.py

api = Api(flask_api)

from .views import tarefa_views
