import json
import requests

from pokemon import Pokemon

generation = 3
url = f"https://pokebuildapi.fr/api/v1/pokemon/generation/{generation}"
payload = ""
response = requests.request("GET", url, data=payload)

pokemon_data = json.loads(response.text)

pokemons = [Pokemon(elm) for elm in pokemon_data]

with open(f'generation{generation}.csv','a', encoding='utf-8') as file:
    file.write(Pokemon.header()+ '\n')
    for elm in pokemons:
        file.write(elm.to_line() + '\n')