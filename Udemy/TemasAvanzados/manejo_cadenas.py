# Manejo de cadenas

# Dividir cadenas split() (parsing)
cadena = 'Hola Mundo'
palabras = cadena.split()
print(palabras)

# ***Buscar y reemplazar***

# Buscar con .find()
posicion = cadena.find('Mundo') # devolver el valor de 5
print(f'Posicion de la cadena Mundo: {posicion}')

# Reemplazar con .replace()
reemplazo = cadena.replace('Mundo', 'Amigo')
print(f'La nueva cadena reemplazada es: {reemplazo}')

# Multiplicacion de cadenas
cadena = 'Hola '
multiplicacion_cadenas = cadena * 3
print(f'El resultado de la multiplicacion de cadenas es: {multiplicacion_cadenas}')

# Metodo .strip() (se usa para limpiar una cadena de saltos, tabulaciones, etc del principio y final)

cadena = '  Hola Mundo    '
cadena_limpia = cadena.strip()
print(f'La cadena de caracteres limpia es: {cadena_limpia}')

# Eliminacion por parametro dentro de strip
cadena = '....Hola Mundo ........'
cadena_limpia = cadena.strip('.')#dentro de () indicamos los caracteres a eliminar
print(f'cadena actual: {cadena}')
print(f'cadena limpia de caracteres especificos es: {cadena_limpia}')