print('##Funcion par##')

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# condicional para probar la funciond desde este modulo
if __name__ == '__main__':
    numero = int(input('Escribe un numero pra saber si es par: '))
    print(f'Es numero par? {es_par(numero)}')