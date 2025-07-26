from Final_Ejer_MundoPC.monitor import Monitor
from Final_Ejer_MundoPC.raton import Raton
from Final_Ejer_MundoPC.teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''


if __name__ == '__main__':
    teclado1 = Teclado('Acer', 'Cable')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('Asus', 25)
    computadora1 = Computadora('Asus', teclado1, raton1, monitor1)
    print(computadora1)

    teclado2 = Teclado('Gamer', 'Bluetooth')
    raton2 = Raton('Gamer', 'Bluetooth')
    monitor2 = Monitor('Gamer', 50)
    computadora2 = Computadora('Gamer', teclado2, raton2, monitor2)
    print(computadora2)
