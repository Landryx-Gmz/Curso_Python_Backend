print('*****Leer archivo con Python*****\n')

nombre_archivo = 'mi_archivo.txt'

# Leer archivo utilizando el metodo readlineas

with open(nombre_archivo, 'r') as  archivo:
    # Leere todas las lineas del archivo
    #print(archivo.readlines())

# Iterar lineas del archivo
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())


# Leer todo el contenido usando el metodo read

print('----Leyendo el contenido con el metodo read----')

with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())