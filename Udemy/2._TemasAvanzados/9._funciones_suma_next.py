# Función sum y next

# ****Funcion sum()******
lista = [1, 2, 3, 4, 5]

# Con la funcion sum() pasando por parametros el nombre de la lista sumamos todos los elementos.

resultado = sum(lista)
print(f'El rsultado de las suma de la lista es: {resultado}')

# Podemos proporcionar un valor inicial
resultado = sum(lista, 20)
print(f"Resultado en la suma con valor inicial 20: {resultado}")

# ****Funcion next()*****
# next(iterador[, valor_predeterminado])

# Transformamos a nuestra listas a iterador para poder recorrerla con la funcion iter()
iterador = iter(lista)

# Con la funcion de next() obtenemos el porximo elemento del iterador 


print(f'El sigiente elemento del iterable es: {next(iterador)}')
print(f'El sigiente elemento del iterable es: {next(iterador)}')
print(f'El sigiente elemento del iterable es: {next(iterador)}')
print(f'El sigiente elemento del iterable es: {next(iterador)}')
print(f'El sigiente elemento del iterable es: {next(iterador)}')
# Siempre llamara al siguiente elemento , siempre y cuando no llamemos mas de lo que la lista tiene si no da error.
