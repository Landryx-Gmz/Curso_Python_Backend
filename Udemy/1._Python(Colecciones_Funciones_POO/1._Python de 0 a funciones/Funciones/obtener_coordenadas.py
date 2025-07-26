print('###Obtener Coordenadas###')

def obtener_coordenadas():
    x,y,z = 10,20,30 # variables locales de la funcion
    return x,y,z
# Llamar a la funcion mediante una variable auxiliar
resultado =obtener_coordenadas()
print(resultado)

# Unpakinmg de la tupla para codigo principal
x1,y2,z3 = resultado

# Imprimimos las variables individuales del codigo principal gracias al unpaking
print(f'Coordenada x = {x1}, coordenada y = {y2}, coordenada z = {z3}')
