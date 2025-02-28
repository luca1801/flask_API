"""
Módulo de visões de tarefas.
"""
from flask_restful import Resource

from flask_api import api


class tarefa_list(Resource):
    def get(self):
        return 'Hello'


api.add_resource(tarefa_list, '/tarefas')
