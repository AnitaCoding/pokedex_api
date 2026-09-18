import requests as consulta

#Almaceno los datos en una variable
pokemon_data = consulta.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
#Convierto los datos a JSON
pokemon_list = pokemon_data.json()

#Creo una lista de diccionarios con el id y los nombres
pokemon_names = []
contador = 1
for i in pokemon_list['results']:
    pokemon_names.append({'id' : contador, 'Nombre': i['name'].capitalize()})
    contador+=1

#Printeo la lista de id con nombre
for i in pokemon_names:
    print(f'{i['id']} - {i['Nombre']}')

#Pedimos al usuario que consulte uno
selection = input('Introduce el id del Pokemon que deseas consultar')
#Se lanza la consulta, da igual si es nombre o id
response = consulta.get(f'https://pokeapi.co/api/v2/pokemon/{selection}')
pokemon_selected = response.json()

#Se printean los datos que queramos.
print(f'Nombre: {pokemon_selected['name'].capitalize()}')
print(f'Peso: {pokemon_selected['weight']}')
print(f'Altura: {pokemon_selected['height']}')
print(f'Tipos: {pokemon_selected['types']}')


#Faaltaría añadir el tipo
#Chequear que lo que introduce el usuario es un número
#Que pueda buscar por nombre, y si lo introduce mal o no existe, informar


