"""Módulo que contém o schema de serialização e desserialização"""
from marshmallow import fields

from flask_api import marsh
from flask_api.models import employer_model


class EmployerSchema(marsh.SQLAlchemyAutoSchema):
    """Employer schema"""

    class Meta:
        """classe interna que especifica o modelo associado ao
        schema e a opção load_instance para carregar
        instâncias do modelo. serializado"""

        model = employer_model.EmployerModel
        fields = (
            'id',
            'name',
            'gender',
            'birth_date',
            'cpf',
            'enterprise',
            'role',
            'email',
            'phone',
        )
        # load_instance = True

    # determinando as regras de validacao
    name = fields.String(required=True)
    gender = fields.String(required=True)
    birth_date = fields.Date(required=True)
    cpf = fields.String(required=True)
    enterprise = fields.String(required=True)
    role = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
