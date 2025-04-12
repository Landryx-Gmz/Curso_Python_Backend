print("comprension de Listas")

# Filtrar solo los numeros pares y generar una nuneva lista con estos valores

numeros = range(1, 10+1)

# Sin usar compreion de listas
numeros_pares=[]
# Iteramos cada elemento de la lista
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f'Numeros pares del 1 al 10 {numeros_pares}')

# usando comprension de listas
# Sintaxis: nueva_lista = [espresion for elemnto in iterable if condicion]
numeros_pares = [numero for numero in numeros if numero % 2 ==0]
print(f"Numeros pares : {numeros_pares}")