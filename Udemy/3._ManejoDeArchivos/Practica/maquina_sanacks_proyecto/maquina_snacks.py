from servicio_snacks import ServiciosSnacks
from snack import Snack


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServiciosSnacks()
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print('***Maquina de Snacks***')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(
                    opcion)  # si el usuario ejecuta la opcion de salir salir = True y saldra del menu caso contrario permancera en el
            except Exception as e:
                print(f'Ocurrio un error: {e}')

    def mostrar_menu(self):
        print(f'''\nMenu:
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar Nuevo Snack al Inventario
        4. Mostrar Inventario Snacks
        5. Salir
        ''')
        return int(input("Elige una opción: "))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Gracias por usar nuestros servicios')
            return True
        else:
            print(f'Opcion invalida {opcion}')
        return False

    def comprar_snack(self):
        id_snack = int(input('Que snack quieres comprar (id)?: '))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'Snack encontrado: {snack}')
        else:
            print(f'Id snack no encontrado: {id_snack}')

    def mostrar_ticket(self):
        if not self.productos:
            print('No hay snacks en el tiket')
            return
        total = sum(snack.precio for snack in self.productos)
        print('----Ticket de venta----')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - ${producto.precio:.2f}')
        print(f'\tTotal -> ${total:.2f}')

    def agregar_snack(self):
        nombre = input('Nombre del snack: ')
        precio = float(input('Precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        id_snack = self.servicio_snacks.generar_id_unico()
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print('Snack agregado correctamente.')


# Programa principal
if __name__ == '__main__':
    maquina_snack = MaquinaSnacks()
    maquina_snack.maquina_snacks()
