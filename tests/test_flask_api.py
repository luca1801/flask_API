import os

import pytest

from flask_api import create_app, db

# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy()


@pytest.fixture
def client():
    appp = create_app(os.getenv('FLASK_CONFIG', 'testing'))
    # app.config['TESTING'] = True
    # db.init_app(app)
    with appp.app_context():
        # yield app.test_client()  # Changed this line to return app.test_client()
        # db.create_all()  # Cria as tabelas no banco de dados de teste
        yield appp.test_client()
        db.session.remove()
        # db.drop_all()  # Limpa o banco de dados após os testes
        db.session.close()


def test_home_page(client) -> None:
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 404
    # Adjust this based on your actual home page content
    # assert b'Welcome' in response.data


def test_employers_list(client) -> None:
    """Test the tarefa list page."""
    response = client.get('/employers/')
    print(response.status_code)
    assert response.status_code == 200
    # assert b'Hello' in response.data
    # print(response.data)


def test_add_employer_post_method(client):
    """Test the POST method for adding a new employer."""

    # Dados do funcionário a ser adicionado
    new_employer_data = {
        'name': 'John Doe',
        'gender': 'Male',
        'birth_date': '1990-01-01',
        'cpf': '12345678901',
        'enterprise': 'Tech Corp',
        'role': 'Developer',
        'email': 'johndoe@example.com',
    }

    # Realiza a requisição POST para adicionar o funcionário
    response = client.post('/employers/', json=new_employer_data)
    # Verifica se o status da resposta é 201 (Created)
    assert response.status_code == 201
    # Verifica se a resposta contém os dados do funcionário adicionado
    response_data = response.get_json()
    assert response_data['name'] == new_employer_data['name']
    assert response_data['email'] == new_employer_data['email']
    assert response_data['cpf'] == new_employer_data['cpf']
