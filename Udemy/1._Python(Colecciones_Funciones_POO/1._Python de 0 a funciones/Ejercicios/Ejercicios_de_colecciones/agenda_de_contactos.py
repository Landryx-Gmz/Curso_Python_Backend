print('Angenda de contactos')

agenda = {
    "Andy": {
        "telefono" : "3355332",
        "email" : "andy@email.com",
        "direccion" : "calle casa 1"
    },
    "Rosa": {
        "telefono" : "3335235235",
        "email" : "rosa@mail.com",
        "direccion" : "calle casas 2"
    },
    "Ania": {
        "telefono" : "323523523",
        "email" : "ania@mail.com",
        "direccion" : "calle casa 3"
    }
}

print(agenda)

# Acceder a la informacion de un contacto en especifico

print(f''' Infomacion de Ania:
    Telefono: {agenda['Ania']['telefono']}
    Email: {agenda['Ania']['email']}
    Direccion:{agenda['Ania']['direccion']}
''')

# Agregar un nuevo contacto

agenda["Ani"] = {
        "telefono" : "3235233",
        "email" : "ani@mail.com",
        "direccion" : "calle casa 4"
    }
print(agenda)

# Eliminar contacto existente
# del agenda['Ani']

agenda.pop('Ani')
print(agenda)

# Mostrar todos los contactos de la agenda
print('\n Lista de contactos en al agenda:')

for nombre, detalles in agenda.items():
    print(f''' Nombre: {nombre}
    Telefono: {detalles['telefono']}
    Email: {detalles['telefono']}
    Direcciona: {detalles['direccion']}
''')