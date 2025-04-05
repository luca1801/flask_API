import os

import pytest
from flask_sqlalchemy import SQLAlchemy

from flask_api import create_app

db = SQLAlchemy()


@pytest.fixture
def client():
    app = create_app(os.getenv('FLASK_CONFIG', 'testing'))
    # app.config['TESTING'] = True
    # db.init_app(app)
    with app.app_context():
        # yield app.test_client()  # Changed this line to return app.test_client()
        # db.create_all()  # Cria as tabelas no banco de dados de teste
        yield app.test_client()
        # db.session.remove()
        # db.drop_all()  # Limpa o banco de dados após os testes


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
