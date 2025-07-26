def sumar(a,b):
    resultado = a+b
    return resultado


# Prueba de la funcion inejecutable fuera del modulo:

if __name__ == '__main__':
    print(f'Prueba función suma: {sumar(5,5)}')