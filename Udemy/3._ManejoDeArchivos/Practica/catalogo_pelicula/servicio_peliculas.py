import os


class ServicioPeliculas:

    def __init__(self):
        self.nombre_archivo = 'peliculas.txt'

    def agregar_pelicula(self):
        pelicula_agregada = input('Dime que pelicula quieres agrear: ')
        try:
            with open(self.nombre_archivo, 'a', encoding='utf8') as archivo:
                archivo.write(f'{pelicula_agregada}\n')
                print('Pelicula agregada correctamente')
        except Exception as e:
            print(f'Error al agregar la pelicula {e}')

    def listar_peliculas(self):
        print('*** Listado de peliculas ***')
        try:
            with open(self.nombre_archivo, 'r', encoding='utf8') as archivo:
                if os.path.exists(self.nombre_archivo):  # Verifica si la lista contiene elementos
                    for pelicula in archivo:
                        print(pelicula.strip())
        except Exception as e:
            print(f'Error {e}')
            print('No hay peliculas por favor cree alguna pelicula')

    def eliminar_peliculas(self):
        if os.path.exists(self.nombre_archivo):  # Verificar si existe un archivo o carpeta
            os.remove('peliculas.txt')
            print('El arichivo de peliculas se elimino correctamente')
        else:
            print('El archivo no existe, no se pudo eliminar')
