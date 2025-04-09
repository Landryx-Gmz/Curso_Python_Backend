#Producto cartesiano de dos listas
colores = ['rojo', 'verde']
tallas = ['S', 'M', 'L']

combinaciones = [(color, talla) for color in colores for talla in tallas]
print(combinaciones)

#-----Avanzado-----

#1.- Aplanar una maztriz
matriz = [[1,2,3], [4,5,6],[7,8,9]]
plana = [num for fila in matriz for num in fila]
print(plana)

#2.- Extraer vocales de una cadena:
cadena = "Lista por comprensión en Python"
vocales = [c for c in cadena.lower() if c in 'aeiouáéíóú']
print(vocales)

#3.- Convertir temperaturas:
Celsius = [0,10,20,30]
fahrenheit = [(temp * 9/5) + 32 for temp in Celsius]
print(fahrenheit)

#4.- Crear una matriz  3x3 ecepto en la diagonal
matriz_identidad = [[1 if i == j else 0 for j in range(3)] for i in  range(3)]
print(matriz_identidad)