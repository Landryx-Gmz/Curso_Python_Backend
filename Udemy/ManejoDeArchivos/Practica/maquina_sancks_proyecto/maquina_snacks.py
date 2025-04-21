from Udemy.ManejoDeArchivos.Practica.maquina_sancks_proyecto.servicio_snacks import ServiciosSnacks


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
                salir = self.ejecutar_opcion()
            except Exception as e:
                print(f'Ocurrio un error: {e}')

    def mostrar_menu(self):
        print(f'''
        1. Comprar snack
        2. Mostrar snack
        3. Agregar Nuevo Snack al Inventario
        4. Inventario Snacks
        5. Salir
        ''')
        return int(input("Elige una opción: "))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comporar_snack()
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
        id_snack = int(input('Que snack quieres comprar (id)?'))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
