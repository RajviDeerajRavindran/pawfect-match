import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200

def test_app_running(client):
    """Test that Flask app is running"""
    response = client.get('/')
    assert response.status_code == 200

def test_response_content_type(client):
    """Test that response is HTML"""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'
