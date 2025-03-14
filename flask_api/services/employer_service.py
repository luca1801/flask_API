"""
A camada de serviços em uma aplicação Flask é usada para
encapsular a lógica de negócios e operações relacionadas
aos dados, separando-as das camadas de apresentação (views)
e de acesso a dados (modelos).
Modulo para acessar o ORM e executar as operações de CRUD
"""
from flask_api import db
from flask_api.models import employer_model


def create_employer(employer):
    """
    Create a new employer.
    """
    new_employer = employer_model.EmployerModel(
        name=employer.name,
        gender=employer.gender,
        birth_date=employer.birth_date,
        cpf=employer.cpf,
        enterprise=employer.enterprise,
        role=employer.role,
        email=employer.email,
        phone=employer.phone,
    )
    db.session.add(new_employer)
    db.session.commit()
    return new_employer
