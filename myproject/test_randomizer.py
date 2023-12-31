import requests
import json

#https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/docs#/

def test_get_books():
    response = requests.get('https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/books/')
    assert response.status_code == 200

def test_get_authors():
    response = requests.get('https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/authors/')
    assert response.status_code == 200

def test_get_author():
    response = requests.get('https://useritem-api-service-eindproject-baisangur-dudayev.cloud.okteto.net/authors/1')
    assert response.status_code == 200



