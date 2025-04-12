# Funciones Lambda

# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2
print(f'Funcion sin lambda para el cuadrado de 5 es: {cuadrado(5)}')

# Funcion lambda(es anonima y  tiene return incorporado)

cuadrado_lambda = lambda x: x ** 2
print(f'La funcion lambda para el cuadrado de 2 es: {cuadrado_lambda(2)}')
print(f'La funcion lambda para el cuadrado de 4 es: {cuadrado_lambda(4)}')