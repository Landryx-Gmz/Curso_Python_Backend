class Pelicula:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Nombre de pelicula = {self.nombre}'
