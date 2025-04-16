#***Manejo de Exepciones****

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception('El denominador es igual a 0')
        resultado = numerador/denominador
        print(f'Resultado de la división es: {resultado}')
    except Exception as e:# Capturando errores generales
        print(f'Ocurrio un error: {e}')
    else:
        print(f'No ocurrio ningun error')

    finally: #Siempre se va a ejecutar
        print("Terminamos de procesar la exepcion\n")


    '''  capturando errores individuales
    except ZeroDivisionError:
        print("Error: no se puede dividir entre 0")
    except TypeError:
        print("Error: los opernados tienen que ser numericos")
    '''

dividir(10,2)
dividir(10, 0)
dividir(10,"hola")