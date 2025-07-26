print('**** PROMEDIO DE CALIFICACIONES ****')

calificaciones = []
numero_de_calificaciones = int(input('Cuantas calificaciones deseas agregar?: '))

for indice in range(numero_de_calificaciones):
    notas = int(input(f'Introduce la calificacion {indice}: '))
    calificaciones.append(notas)

# Imprimir calificaciones:
print(f'Tus calificaciones proporcionadas son: {calificaciones}')

# Calculo Promedio
suma_calificaciones = sum(calificaciones)

promedio = suma_calificaciones / numero_de_calificaciones

# Resultado
print(f'El promedio de tus calificaciones es: {promedio}')
