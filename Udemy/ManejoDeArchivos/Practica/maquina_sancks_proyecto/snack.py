class Snack:
    contador_snack = 0

    def __init__(self, nombre='', precio = 0.0):
        Snack.contador_snack += 1
        self.id_snak = Snack.contador_snack
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return (f'Snack: id_snack = {self.id_snak}, nombre = {self.nombre},'
        f'precio = {self.precio}')

    def escribir_snack(self):
        return f'{self.id_snak},{self.nombre},{self.precio}'