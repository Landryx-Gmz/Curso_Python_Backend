# Funciones Lambda

# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2


print(f'Funcion sin lambda para el cuadrado de 5 es: {cuadrado(5)}')

# Funcion lambda(es anonima y  tiene return incorporado)

cuadrado_lambda = lambda x: x ** 2
print(f'La funcion lambda para el cuadrado de 2 es: {cuadrado_lambda(2)}')
print(f'La funcion lambda para el cuadrado de 4 es: {cuadrado_lambda(4)}')

# Con ma y lambda
# Acreamos una lista de numeror
numeros = [1, 2, 3, 4, 5]

# Aplicar una funicion lamba para obtener el cuadrado de cada numero

cuadrados = list(map(lambda x: x ** 2, numeros))
print(f'Resultado de usar map y lambda: {cuadrados}')

# Con fliter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Resultado de usar filter para filtrar numero pars: {pares}')
