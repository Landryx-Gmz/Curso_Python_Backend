print('----Boletin Informativo----')

suscriptores = set()

num_suscriptores = int(input('Cuantos suscriptores quieres agregar: '))

for _ in range(num_suscriptores):
    suscriptores.add(input(f'Nuevo suscriptor (email) {_ + 1}: '))

print(f'Lista de suscriptores iniciales:')
for suscriptor in suscriptores:
    print(suscriptor)


#Verificar si nuevo suscriptor esta en set

nuevo_suscriptor = input('Ingrese nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El suscriptior ya existe en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptior a sido agregado a la lista {nuevo_suscriptor}')

#Eliminar suscriptor
for suscriptor in suscriptores:
    print(suscriptor)
suscriptor_eliminar = input('Suscriptor a eliminar: ')
if suscriptor_eliminar in suscriptores:
    suscriptores.remove(suscriptor_eliminar)
    print(f'El suscriptor /{suscriptor_eliminar}/ a sido eliminado')
else:
    print('No existe el suscriptor que desea eliminar')

for suscriptor in suscriptores:
    print(suscriptor)
print(f'El total de suscriptores es: {len(suscriptores)}')
