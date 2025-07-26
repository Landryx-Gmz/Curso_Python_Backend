# Juego numero secreto
import random

numero_aleatorio = random.randint(1, 50)

print('****Bienvendio al juego de adivinar el numero aleatorio****')
MAXIMO_DE_INTENTOS = 4
numero_intentos = 0
numero_ingresado = None

while numero_ingresado != numero_aleatorio and numero_intentos < MAXIMO_DE_INTENTOS:
    numero_ingresado = int(input('Porfavor ingrese el numero que cree que es el correcto: '))
    numero_intentos += 1
    if numero_aleatorio > numero_ingresado:
        print('El numero secreto es MAYOR que el ingresado, intentelo de nuevo')
        print(f'Llevas {numero_intentos} INTENTOS\n')

    elif numero_aleatorio < numero_ingresado:
        print('El numero secreto es MENOR que el ingresado, intentelo de nuevo')
        print(f'Llevas {numero_intentos} INTENTOS\n')

if numero_ingresado == numero_aleatorio:
    print(f'Correcto el numero secreto es: {numero_aleatorio} y lo consegistes en {numero_intentos} INTENTOS')
else:
    print(f'Game Over, as superado el maximo de intentos:{numero_intentos} el numero secreo era: {numero_aleatorio}')
