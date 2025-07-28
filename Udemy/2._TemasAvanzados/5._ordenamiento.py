print('*** Ordenamiento en Python ***')

# sintaxis: sorted(iterable, key= None, reverse=False)

empleados = ['Juan', 'Pedro', 'Maria']

# Ordenar la lista

empleados_ordenados = sorted(empleados)

print(f'Empleados ordenados: {empleados_ordenados}')

# Ordenamos la lista al reves con reverse = True

empleados_ordenados = sorted(empleados_ordenados, reverse=True)
print(f'Empleados ordenados alreves: {empleados_ordenados}')

# Ordenar un dicccionario (una llave)

empleados_dict = [
    {'nombre': 'Juan', 'salario': 3000},
    {'nombre': 'Maria', 'salario': 2500},
    {'nombre': 'Pedro', 'salario': 3500}
]

empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x['salario'])
print(f'Empleados ordenads por salarios: {empleados_ordenados_por_salario}')
