print('### Suma con argumentos variables ###')


# Funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total


cantidad = int(input('Por favor dime cuantos numeros quieres ingresar: '))

numeros = []

for i in range(cantidad):
    numero = float(input(f'dime el numero #{i + 1}: '))
    numeros.append(numero)


# LLamamos a la funcion de sumar
resultado = sumar(*numeros)

print(f'El resultado total es: {resultado}')