print('#### Funcion para calcular el factorial de un numero ###')

# Funcion
def factorial_num(numero):
    #caso base
    if numero == 1 or numero == 0:
        print(f'El resultad factorial parcial {numero} es: 1')
        return 1

    # Caso recursivo
    else:
        factorial_parcial = numero * factorial_num(numero -1)
        print(f'El resultad factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

if __name__ == '__main__':
    # solicitar al usuario numero a calcular:
    numero = int(input('Dime el numero que desea calcular su factorial: '))

    # Comprovamos que el numero es positivo:
    if numero < 0:
        print('Error el numero no es positivo')

    else:
        # Llamamaos a la funcion factorial_recursivo para el calculo mediante una variable auxiliar
        resultado = factorial_num(numero)
        print(f'el factorial de {numero} es: {resultado}')





