import sys
import os

# Add the parent directory of `tests/` to sys.path so it can find app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_health_check():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_ip():
    client = app.test_client()
    response = client.get('/ip')
    assert response.status_code == 200
    assert b"ip" in response.data

def test_headers():
    client = app.test_client()
    response = client.get('/headers')
    assert response.status_code == 200
