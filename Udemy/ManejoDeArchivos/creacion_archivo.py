# Crear un archivo
nombre_archivo = 'mi_archivo.txt'

# Abrir el archivo en modo escritura ('w')
archivo = open(nombre_archivo, 'w')
# Agregamos informacion con .write()
archivo.write('Hola como estas\n')
archivo.write("estoy agregando informacion al archivo\n")
archivo.close()#cerramos el flujo

print(f'Se creo el archifo: {nombre_archivo}')