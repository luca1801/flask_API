"""
Responsável por tratar requisições http, validar os dados
e criar instâncias do objeto.
"""
from flask import jsonify, make_response, request
from flask_restful import Resource

from flask_api import api

from ..entities import employer
from ..schemas import employer_schema
from ..services import employer_service


class EmployerList(Resource):
    """
    Employer list resource.
    """

    def get(self):
        return 'Hello'

    def post(self):
        es = employer_schema.EmployerSchema()
        validate = es.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['name']
            genero = request.json['gender']
            data_nasc = request.json['birth_date']
            cpf = request.json['cpf']
            empresa = request.json['enterprise']
            cargo = request.json['role']
            email = request.json['email']
            telefone = request.json['phone']
            new_employer = employer.employer(
                name=nome,
                gender=genero,
                birth_date=data_nasc,
                cpf=cpf,
                enterprise=empresa,
                role=cargo,
                email=email,
                phone=telefone,
            )
            result = employer_service.create_employer(new_employer)
            return make_response(es.jsonify(result), 201)


api.add_resource(EmployerList, '/employers')
