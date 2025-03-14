# import pytest

# from flask_api import create_app


# @pytest.fixture
# def client():
#     flask_api = create_app()
#     flask_api.config['TESTING'] = True
#     with flask_api.app_context():
#         yield flask_api


# def test_home_page(client) -> None:
#     """Test the home page."""
#     response = client.get('/')
#     assert response.status_code == 404
#     # Adjust this based on your actual home page content
#     # assert b'Welcome' in response.data


# def test_employers_list(client) -> None:
#     """Test the tarefa list page."""
#     response = client.get('/employers')
#     assert response.status_code == 200
#     assert b'Hello' in response.data
#     # print(response.data)
