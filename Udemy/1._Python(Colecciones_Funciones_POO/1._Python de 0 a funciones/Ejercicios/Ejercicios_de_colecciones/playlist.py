print('PLAYLIST')

lista_reproduccion = []

lista_reproduccion.append('Dream on - Aerosmith')
lista_reproduccion.append('We well roch you - Queen')
lista_reproduccion.append('Ride on - ACDC')

# Agregar canciones:
numero_canciones = int(input('Cuantas caciones quieres agregar?: '))

for indice in range(numero_canciones):
    cancion = input(f'Agrega la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Ordenar en orde alfabetico
lista_reproduccion.sort(reverse=True)  # opcion orden decendente

# Enseñar la lista
print(f'\nLista en orden alfabetico inverso:')
for cancion in lista_reproduccion:
    print(f'*{cancion}')
