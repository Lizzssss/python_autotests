import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
TOKEN = 'e8d39663bff5aa047b8aed263e561e85'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_code():

# Проверка кода 200
    
    response = requests.get(url=f'{URL}/trainers', params={'level':1})
    assert response.status_code == 200, 'Unexpected status code'

def test_get_trainers_response():

# Проверка имени тренера по id
    
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':4692})
    assert response.json()['trainer_name'] == 'Liza', ''