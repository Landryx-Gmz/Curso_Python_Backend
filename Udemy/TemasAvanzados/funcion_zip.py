# Funcion zip

nombres = ['Juan', 'Ana', 'Pedro']
edades = [30, 25, 35]
ciudades = ['Madrid', 'Barcelona', 'Sevilla']

# Combinar los elementos correspondientes usando la función zip
personas = zip(nombres, edades, ciudades)

#Iterar sobre el resultado de la funcion zip(si no se itera solo nos dara el nombre o hash del objeto)
for persona in personas:
    print(persona)