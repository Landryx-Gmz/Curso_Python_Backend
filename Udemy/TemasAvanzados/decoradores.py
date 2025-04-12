# Decoradores en python

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la funcion saludar')
        resultado = funcion(*args, **kwargs) # llamamos anuestra funcion
        print('Despues de llamar la funcion saludar')
        return resultado
    return wrapper

@decorador
def saludar (nombre):
    print(f'Hola {nombre}')

saludar('Andres')

# Ejemplo:
def palabras_descripcion(funcion):
    def envoltorio_wrapper(*args, **kwargs):
        print('Ejecutando Programa de calculo')
        funcion(*args, *kwargs)
        print('Gracias por usar nuestro programa')
    return envoltorio_wrapper

@palabras_descripcion
def descript(operador):
    print(f'Se utlizara {operador} para el calculo')

@palabras_descripcion
def suma(x,y):
    calculo = x + y
    print(f'La suma de {x} y de {y} es: {calculo}')

descript("suma")
suma(4,6)