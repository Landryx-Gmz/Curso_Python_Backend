print('---Gestion de Inventario---')

inventario = []
nuemero_productos = int(input("Cuantos productos desea agregar?: "))

for indice in range(nuemero_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre= input('Nombre: ')
    precio= input('Precio: ')
    cantidad= input('Cantidad: ')
    #Crear el diccionario con el detalle del producto
    producto = {'id':indice,'Nombre':nombre,'Precio':precio,'Cantidad':cantidad}
    #Agregamos el nuevo producto al inventario
    inventario.append(producto)

#Mostar inventario simplificado
print(inventario)

# Buscar un producto por ID

# Buscar un producto por ID
id_buscar = int(input('\nProporciona la id del producto a buscar: '))
producto_encontrado = None

for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break  # ¡ya lo encontramos, no hay que seguir buscando!

if producto_encontrado:# Cuando esta la variable sola significa -  tiene un producto (es decir, no es None

    print('Informacion del producto encontrado:')
    print(f''' id: {producto_encontrado.get('id')},
        Nombre: {producto_encontrado.get('Nombre')},
        Precio: {producto_encontrado.get('Precio')},
        Cantidad: {producto_encontrado.get('Cantidad')}
''')
else:
    print(f'Producto con id {id_buscar} no encontrado')

# Inventario actualizado

print('Inventario Actualizado:')
for producto in inventario:
    print(f''' id: {producto.get('id')},
        Nombre: {producto.get('Nombre')},
        Precio: {producto.get('Precio')},
        Cantidad: {producto.get('Cantidad')}
    ''')