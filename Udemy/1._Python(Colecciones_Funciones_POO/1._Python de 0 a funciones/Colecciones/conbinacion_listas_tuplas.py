print('***COMBINACION LISTAS Y TUPLAS***')

# Definir lista que almacena tuplas de productos

productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'calcetines', 40.00),
]

#Imprimimos informacion de cada producot
#Calculamos el precio total
total = 0
for producto in productos:
    id, descripcion, precio = producto #Unpaking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = { precio}')
    total += precio
print(f'El precio total es de: {total}')



