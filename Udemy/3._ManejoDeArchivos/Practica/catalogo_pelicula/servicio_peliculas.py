import os


class ServicioPeliculas:
    nombre_archivo = 'peliculas.txt'

    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self):
        pelicula_agregada = input('Dime que pelicula quieres agrear: ')

        self.peliculas.append(pelicula_agregada)
        print('Pelicula agregada correctamente')

    def agregar_peli_archivo(self):
        pass

    def listar_pelicula(self):
        print('*** Listado de peliculas ***')
        if self.peliculas:  # Verifica si la lista contiene elementos
            for pelicula in self.peliculas:
                print(pelicula)
        else:
            print('No hay peliculas por favor cree alguna pelicula')

    def eliminar_peliculas(self):
        if os.path.exists(self.nombre_archivo):  # Verificar si existe un archivo o carpeta
            os.remove('peliculas.txt')
            print('El arichivo de peliculas se elimino correctamente')
        else:
            print('El archivo no existe, no se pudo eliminar')
