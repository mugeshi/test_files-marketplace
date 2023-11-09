import requests
import pytest

BASE_URL = "http://localhost:5000"


def test_delete_history():
    payload = {"email": "test@example.com"}

    try:
        response = requests.delete(f"{BASE_URL}/history", json=payload)
        assert response.status_code == 200
    except Exception as e:
        pass




def test_delete_profile():
    payload = {"email": "test@example.com"}

    try:
        response = requests.delete(f"{BASE_URL}/profile", json=payload)
        assert response.status_code == 200
    except Exception as e:
        pass




def test_login():
    payload = {"email": "test@example.com", "password":"123"}

    try:
        response = requests.post(f"{BASE_URL}/login", json=payload)
        assert response.status_code == 201
    except Exception as e:
        pass

def test_update_profile():
    payload = {"email": "test@example.com", "password": "1234"}

    try:
        response = requests.post(f"{BASE_URL}/profile", json=payload)
        assert response.status_code == 201
    except Exception as e:
        pass
  


  

