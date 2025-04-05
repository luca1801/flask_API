"""
Responsável por tratar requisições http, validar os dados
e criar instâncias do objeto.
"""
# from flask import jsonify, make_response, request
# from flask_restful import Resource
from flask_restx import Resource, fields

from ..entities import employer
from ..schemas.employer_schema import employer_schema, employers_schema
from ..services import employer_service
from .namespace import ns

# Request/response models for Swagger documentation
employer_model = ns.model(
    'Employer',
    {
        'id': fields.Integer(readOnly=True),
        'name': fields.String(required=True),
        'gender': fields.String(required=True),
        'birth_date': fields.Date(required=True),
        'cpf': fields.String(required=True),
        'enterprise': fields.String(required=True),
        'role': fields.String(required=True),
        'email': fields.String(required=True),
    },
)

employer_post_model = ns.model(
    'EmployerPost',
    {
        'name': fields.String(required=True),
        'gender': fields.String(required=True),
        'birth_date': fields.Date(required=True),
        'cpf': fields.String(required=True),
        'enterprise': fields.String(required=True),
        'role': fields.String(required=True),
        'email': fields.String(required=True),
    },
)


@ns.route('/')
class EmployerList(Resource):
    """
    Employer list resource.
    """

    @ns.marshal_list_with(employer_model)
    def get(self):
        # return 'Hello'
        employers = employer_service.list_employer('all')
        return employers_schema.dump(employers)

    @ns.expect(employer_post_model)
    @ns.marshal_with(employer_model, code=201)
    def post(self):
        data = ns.payload

        if employer_service.check_if_exists(data):
            ns.abort(400, 'Email already registred')

        new_employer = employer.employer(
            name=data['name'],
            gender=data['gender'],
            birth_date=data['birth_date'],
            cpf=data['cpf'],
            enterprise=data['enterprise'],
            role=data['role'],
            email=data['email'],
        )
        result = employer_service.create_employer(new_employer)
        return employer_schema.dump(result), 201

        # es = employer_schema.EmployerSchema()
        # es = employer_schema()
        # validate = es.validate(request.json)
        # if validate:
        #     # print('abacate')
        #     return make_response(jsonify(validate), 400)
        # else:
        #     nome = request.json['name']
        #     genero = request.json['gender']
        #     data_nasc = request.json['birth_date']
        #     cpf = request.json['cpf']
        #     empresa = request.json['enterprise']
        #     cargo = request.json['role']
        #     email = request.json['email']
        #     telefone = request.json['phone']
        #     new_employer = employer.employer(
        #         name=nome,
        #         gender=genero,
        #         birth_date=data_nasc,
        #         cpf=cpf,
        #         enterprise=empresa,
        #         role=cargo,
        #         email=email,
        #         phone=telefone,
        #     )
        #     result = employer_service.create_employer(new_employer)
        #     return make_response(es.jsonify(result), 201)


# api.add_resource(EmployerList, '/employers')
