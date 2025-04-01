import os

import pytest

from flask_api import create_app


@pytest.fixture
def client():
    app = create_app(os.getenv('FLASK_CONFIG', 'testing'))
    # app.config['TESTING'] = True
    with app.app_context():
        yield app.test_client()  # Changed this line to return app.test_client()


def test_home_page(client) -> None:
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 404
    # Adjust this based on your actual home page content
    # assert b'Welcome' in response.data


def test_employers_list(client) -> None:
    """Test the tarefa list page."""
    response = client.get('/employers')
    assert response.status_code == 200
    # assert b'Hello' in response.data
    # print(response.data)
