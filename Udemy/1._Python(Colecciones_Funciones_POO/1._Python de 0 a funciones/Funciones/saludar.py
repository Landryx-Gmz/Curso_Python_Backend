print('***Saludar***')

# 1. Definir una funcion lllamada saludar

def saludar(mensaje):
    print(f'Menjsaje recibido: {mensaje}')
    return  'termino la ejecucion de la funcion saludar'

# 2. Llamar la funicion (ya tiene que estar definida)
argumento = 'hola desde la funcion saludar'
valor_devuelto=saludar(argumento)
print(f'valo devuelto de la fucncion : {valor_devuelto}')
