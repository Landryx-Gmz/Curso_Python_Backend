print("###Funcon con argumentos por nombre###")

def crear_persona(nombre, apellido = '', edad = 0):
    print(f'nombre = {nombre}, apellido = {apellido}, edad = {edad}')

crear_persona(edad=13,nombre='Andy')