import requests
import json


def test_get_books():
    response = requests.get('https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/books/')
    assert response.status_code == 200

def test_get_authors():
    response = requests.get('https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/authors/')
    assert response.status_code == 200

def test_get_author():
    response = requests.get('https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/authors/1')
    assert response.status_code == 200

#testen voor niet bestaande authors
def test_get_author_nonexistant():
    response = requests.get('https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/authors/99999')
    #404 niet gevonden, want hetbestaat niet
    assert response.status_code == 404

API_BASE_URL = "https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net"

def get_access_token():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    request_data = {
        "grant_type": "password",
        "username": "test@hotmail.com",
        "password": "password"
    }

    token_request = requests.post(f"{API_BASE_URL}/token", data=request_data, headers=headers)
    return json.loads(token_request.text)["access_token"]

def test_users_me():
    access_token = get_access_token()

    # headers
    headers_with_token = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    # GET request naar /users/me
    get_request = requests.get(f"{API_BASE_URL}/users/me", headers=headers_with_token)

    #testen
    assert get_request.status_code == 200

#testen voor een lege token
def test_users_me_no_token():
    access_token = 'empty'

    # headers
    headers_with_token = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    # GET request naar /users/me
    get_request = requests.get(f"{API_BASE_URL}/users/me", headers=headers_with_token)

    #testen
    assert get_request.status_code == 401