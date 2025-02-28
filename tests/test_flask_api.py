import pytest

from flask_api import flask_api


@pytest.fixture
def client():
    flask_api.config['TESTING'] = True
    with flask_api.test_client() as client:
        yield client


def test_home_page(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 404
    # Adjust this based on your actual home page content
    # assert b'Welcome' in response.data


def test_tarefa_List(client):
    """Test the tarefa list page."""
    response = client.get('/tarefas')
    assert response.status_code == 200
    assert b'Hello' in response.data
    # print(response.data)
