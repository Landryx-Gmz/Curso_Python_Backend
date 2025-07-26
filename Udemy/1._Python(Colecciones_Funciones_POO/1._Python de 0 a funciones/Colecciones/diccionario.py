# dict - diccionario

print('***Diccionarios en python***')

# Crea un dicionario de persona con llave y valor

persona = {
    'nombre': 'Andy',
    'edad': 36,
    'ciudad': 'Ecuador'
}

print(f'Dicionario de persona: {persona}')

# Acceder a los elementgos del diccionario

print(f'nombre: {persona['nombre']}')
print(f'edad: {persona['edad']}')
print(f'ciudad: {persona['ciudad']}')

#Modificar diccionario
persona['edad'] = 37

print(f'Dicionario de persona: {persona}')

#Agregar elemento

persona['profecion'] = 'Ingeniero'

print(f'Dicionario de persona: {persona}')

# Eliminar elemnto

del persona['ciudad']

print(f'Dicionario de persona: {persona}')

#Iterar diccionario

for clave, valor in persona.items():
    print(f'clave {clave} y valor: {valor}')