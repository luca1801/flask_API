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


def list_employer(employer):
    # employer = employer
    if employer == 'all':
        employer_bd = employer_model.EmployerModel.query.all()
        return employer_bd
    else:
        employer_bd = employer_model.EmployerModel.query.filter_by(
            nome=employer['name']
        ).first()
        return employer_bd
    
def check_if_exists(data):
    if employer_model.EmployerModel.query.filter_by(
        email=data['email']
        ).first():
        return True
    else:
        return False
        
