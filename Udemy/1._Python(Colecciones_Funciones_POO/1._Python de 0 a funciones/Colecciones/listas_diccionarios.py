print('###Listas y diccionarios###')

personas = [
    {
        'nombre': 'Andy',
        'apellido': 'Gomez',
        'edad': 36
    },
    {
        'nombre':'Rosa',
        'apellido':'Montoya',
        'edad':35
    },
]
print(personas)

#Acceder a un diccionario
print(f'\n--Acceder a un dicionario--')
print(f'''-Nombre: {personas[0].get('nombre')}
        -Apelldio: {personas[0].get('apellido')}
        -Edad: {personas[0].get('edad')}
''')

for contador, personas in enumerate(personas):
    print(f'''Indice: {contador +1} :
    Contienes a la persona: {personas.get('nombre'),
    personas.get('apellido'),
    personas.get('edad')}''')