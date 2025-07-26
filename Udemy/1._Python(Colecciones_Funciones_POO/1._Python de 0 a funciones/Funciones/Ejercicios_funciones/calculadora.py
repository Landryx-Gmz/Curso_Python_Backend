print('*** Calculadora ***')
# Funcion recolector de valores
def recolectar_valores():
    valor1 = float(input('Dame el valor 1: '))
    valor2 = float(input('Dame el valor 2: '))
    return valor1,valor2
# Funcion Sumar
def funcion_sumar():
    valor1, valor2 = recolectar_valores()
    resultado = valor1 + valor2
    print(f'El resultado de la suma de {valor1} y {valor2} es = {resultado}' )
# Funcion Restar
def funcion_restar():
    valor1, valor2 = recolectar_valores()
    resultado = valor1 - valor2
    print(f'El resultado de la resta de {valor1} y {valor2} es = {resultado}' )
# Funcion Multiplicar
def funcion_multiplicar():
    valor1, valor2 = recolectar_valores()
    resultado = valor1 * valor2
    print(f'El resultado de la multiplicacion de {valor1} y {valor2} es = {resultado}' )

# Funcion Dividir
def funcion_dividir():
    valor1, valor2 = recolectar_valores()
    if valor2 == 0:
        print('No se puede dividir por cero')
        return
    resultado = valor1 / valor2
    print(f'El resultado de la division de {valor1} y {valor2} es = {resultado}' )
# Programa principal:
if __name__ == '__main__':# Bucle del menu
    while True:
        print(f'''\nOperaciones que puedes realizar:
                1. Suma
                2. Resta
                3. Multiplicacion
                4. Division
                5. Salir''')
        opcion = int(input('Elige una opcion: '))

        if opcion == 1:
            funcion_sumar()
        elif opcion == 2:
            funcion_restar()
        elif opcion == 3:
            funcion_multiplicar()
        elif opcion == 4:
            funcion_dividir()
        elif opcion == 5:
            print('Hasta Luego')
            break
        else:
            print('Opcion invalida eliga una opcion correcta')