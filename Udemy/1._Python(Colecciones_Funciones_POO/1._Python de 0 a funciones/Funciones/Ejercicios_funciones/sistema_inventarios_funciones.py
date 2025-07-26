print('#### SISTEMA INVENTARIO CON FUNCIONES ####')

# Inventario del almacen

invetario =[
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]


# Funcion para mostrar el inventario:

def mostrar_inventario():
    print('Invetarioi del almacen:')
    for producto in invetario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: {producto.get('precio')}, Cantidad: {producto.get('cantidad')}')


# Funcion pera agregar un nuevo producto:
def agregar_producto():
    print('*** Agregar Producto ***')
    id = int(input('Ingrese el ID: '))
    nombre = input('Ingrese el nombre: ')
    precio = float(input('Ingrese el precio: '))
    cantidad = int(input('Ingrese la cantidad: '))
    nuevo_producto = {'id': id,'nombre':nombre,'precio':precio,'cantidad':cantidad}
    invetario.append(nuevo_producto)
    print('Producto agregado correctamente')


# Funcion para buscar por id
def buscar_producto_por_id():
    print('### Buscar producto por ID:')
    id_a_buscar = int(input('Ingrese el ID a buscar: '))

    for producto in invetario:
        if producto.get('id')== id_a_buscar:
            print(f'\n--Informacion del producto encontrado:--')
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: {producto.get('precio')}, Cantidad: {producto.get('cantidad')}')
            return
    print(f'\nProducto con ID: {id_a_buscar} no encontrado')
#Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n ---Menu---
        1. Mostrar inventario.
        2. Agregar producto.
        3. Buscar producto por ID.
        4. Salir.
        ''')
        opcion = int(input('Eliga una de las opciones: '))

        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto_por_id()
        elif opcion == 4:
            print('Hasta luego')
            break
        else:
            print('Opcion invalida por favor eliga una de las opciones del menu')

