# Crear un archivo
nombre_archivo = 'mi_archivo.txt'

# Abrir el archivo en modo escritura ('w')

# Bloque with (se utiliza para hacer que un archivo tenga apertura y cierre sin utilizar .close())

# Sintaxis:
#   with open(nombre del archivo, modo) as variableAuxiliar:
#       bloque con sangria de lo que queramos operar sin open() ni close()

with open(nombre_archivo, 'w') as archivo:
    archivo.write('Hola como estas\n')
    archivo.write("estoy agregando informacion al archivo\n")
    archivo.write("con el bloque with\n")

# Ejemplo sin with:
'''
archivo = open(nombre_archivo, 'w')
# Agregamos informacion con .write()
archivo.write('Hola como estas\n')
archivo.write("estoy agregando informacion al archivo\n")
#archivo.close()#cerramos el flujo
'''
print(f'Se creo el archifo: {nombre_archivo}')