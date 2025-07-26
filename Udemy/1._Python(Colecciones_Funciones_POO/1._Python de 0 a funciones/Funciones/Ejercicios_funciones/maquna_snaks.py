print(F'{'*'*15} MAQUINA DE SNAKS {'*'*15}')

Snacks = [
    {'id':1, '->': 'Papas', 'precio':30},
    {'id':2, '->': 'Refresco', 'precio':50},
    {'id':3, '->': 'Sandwich', 'precio':120},
]

snack_comprados =[]

# Funcion mostrar snack
def mostrar_snacks():
    print('----Snacks Disponibles----')
    for producto in Snacks:
        print(f'Id:{producto.get('id')} -> {producto.get('->')} - Precio: {producto.get('precio')}')

# Funcion Comprar snack
def comprar_sanck():
    snack_a_comprar = int(input('Que snack quieres? (id): '))
    for producto in Snacks:
        if snack_a_comprar == producto.get('id'):
            snack_comprados.append(producto)
            print(f'Se a añadido correctamente el snack:  {producto.get('->')}')
            mostrar_snacks()
            return

    print('No se encontro ningun snack con el id proporcionado')


# Funcion mostrar ticket
def mostrar_ticket():
    print('---- Ticket de compra ----')
    print('\nSnack comprados:')
    total = 0 #variable que suma el precio
    for producto in snack_comprados:
        print(f'{producto.get('->')} - Precio: {producto.get('precio')}')
        total += producto['precio']
    print(f'Total a pagar {total}')

#Programa principal
if __name__ == '__main__':
    while True:

        print(f'''\nMENU:
        1. Mostrar Snacks
        2. Comprar Snacks
        3. Mostrar Ticket
        4. Salir
''')
        opcion = int(input('Elija una opcion: '))

        if opcion == 1:
            mostrar_snacks()
        elif opcion ==2:
            comprar_sanck()
        elif opcion ==3:
            mostrar_ticket()
        elif opcion ==4:
            print('Hasta luego')
            break
        else:
            print('Opcion invalida por favor eliga una opcion correcta:')
