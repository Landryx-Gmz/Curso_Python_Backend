print('###Regresar una tupla de valores desde una funcion###')

# Definicion de la fucion
def persona_mayusculas(nombre,apellido,edad):
    print('Esta funcion devuelve los valores en mayusculas y en una tupla')
    return nombre.upper(),apellido.upper(),edad #Al retornar con comas se crea la tupla

#Unpaking
nombre,apelldio,edad = persona_mayusculas('andy','gomez',36)
print(f'resultado de persona es: nombre={nombre}, apellido={apelldio}, edad={edad}')