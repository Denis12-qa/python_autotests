import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'this_is_my_token'
HEADER = {'Content-Type' :'application/json', 'trainer_token' :TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "Login",
    "password": "Password",
    "password_re": "Password"
}
body_confirmation =  {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''
  
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create  = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text) 

pokemon_id = response_create.json()['id']

print(pokemon_id)
