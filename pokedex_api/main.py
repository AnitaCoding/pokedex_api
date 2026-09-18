import requests as consulta

pokemon_data = consulta.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
#print(pokemon_data.json())
pokemon_list = pokemon_data.json()
pokemon_names = []

contador = 1
for i in pokemon_list['results']:
    pokemon_names.append({'id' : contador, 'Nombre': i['name']})
    contador+=1

for i in pokemon_names:
    print(f'{i['id']} - {i['Nombre']}')

