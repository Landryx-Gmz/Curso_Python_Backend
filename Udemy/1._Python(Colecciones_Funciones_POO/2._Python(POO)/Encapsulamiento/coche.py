class Coche2:
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def conducir(self):
        print(f''' Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    # Getters y Setters

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


if __name__ == '__main__':
    # Creacion de un primer coche:
    coche1 = Coche2('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # Utilizamos el concepto de encapsulamiento (get/set)

    coche1.set_marca('Toyota2')
    coche1.set_color('Negro')
    coche1.set_modelo('Yaris2')
    coche1.conducir()
    print(
        f'Atributos del coche1: {coche1.__dict__}')  # __dict__palabara magica reservadad para ver los atributos de un objeto
