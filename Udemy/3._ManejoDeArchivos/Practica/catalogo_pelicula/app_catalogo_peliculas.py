from servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def maquina_peliculas(self):
        salir = False
        print('*** App Catalogo de peliculas ***')
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except ValueError:
                print('Error: las opciones solo pueden ser numeros del menu')
            except Exception as e:
                print(f'ocurrio un error {e}')

    def mostrar_menu(self):

        print(f'''\nMenu:
        1. Agregar pelicula
        2. Listar peliculas
        3. Eliminar catalogo pliculas
        4. Salir
        ''')
        return int(input("Elige una opción: "))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.servicio_peliculas.agregar_pelicula()
        elif opcion == 2:
            self.servicio_peliculas.listar_pelicula()
        elif opcion == 3:
            self.servicio_peliculas.eliminar_peliculas()
        elif opcion == 4:
            print('Gracias por usar nuestros servicios')
            return True
        else:
            print(f'Opcion invalida {opcion}')
        return False


# Programa principal
if __name__ == '__main__':
    app_catalo = AppCatalogoPeliculas()
    app_catalo.maquina_peliculas()
