import requests

URL = 'https://api.pokemonbattle.me:9104'
TOKEN = 'e8d39663bff5aa047b8aed263e561e85'

#Первый запрос: Создание покемона

response = requests.post(url=f'{URL}/pokemons', json={
    "name": "generate",
    "photo": "generate"
}, headers= {'trainer_token': TOKEN, 
             'Content-Type': 'application/json'})

print(response.json())

#Второй запрос: Смена имени покемона

response = requests.put(url=f'{URL}/pokemons', json={
    "pokemon_id": "28019",
    "name": "Newone",
    "photo": "https://dolnikov.ru/pokemons/albums/006.png"
}, headers= {'trainer_token': TOKEN, 
             'Content-Type': 'application/json'})

print(response.json())

#Третий запрос: Поймать покемона в покебол

response = requests.post(url=f'{URL}/trainers/add_pokeball', json={
    "pokemon_id": "28019"
}, headers= {'trainer_token': TOKEN, 
             'Content-Type': 'application/json'})

print(response.json())