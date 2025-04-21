import os.path
from snack import Snack


class ServiciosSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []
        # Revisar si existe el archivo snacks
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            # Si existe, obtenemos los snacks del archivo
            self.snacks = self.obtener_snacks()
        # sino, cargamos algunos snacks iniciales
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snaks_iniciales = [
            Snack('Papas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 120)
        ]
        self.snacks.extend(snaks_iniciales)
        self.guardar_snacks_archivo(snaks_iniciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    id_snack, nombre, precio = linea.strip().split()
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error al leer archivo de snacks: {e}')
        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks
