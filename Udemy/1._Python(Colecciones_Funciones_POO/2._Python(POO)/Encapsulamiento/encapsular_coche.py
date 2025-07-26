class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca  # Atributo  publico
        self._modelo = modelo  # Atributo  protegido
        self.__color = color  # Atributo  privado

    def conducir_coche(self):
        print(f'''Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Coror: {self.__color}''')


# Principal
if __name__ == '__main__':
    # Creacion de un primer coche:
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir_coche()
    # Gracias a encapsular los atributos el IDE no nos recomendara poder acceder a ningun atributo que no sea publico para poder modificarlo
    coche1.marca = 'Toyota2'
    coche1.conducir_coche()
    # Sin envargo si escribimos el atributo PROTEGIDO podremos cambiarlo aunque el IDE no nos lo recomiendo eso se considera MALAS PRACTICAS!
    coche1._modelo = 'Yaris2'  # NO RECOMENDABLE
    coche1.conducir_coche()

    # Pero el atributo PRIVADO python ignora los cambios aunque los escribamos
    print('En atributo Privado se ignora los cambios ')
    coche1.__color = 'Rojo'
    coche1.conducir_coche()

    # Esta es la unica manera de cambiar los atributos privados ya que en python no existe realmente las restricciones de encapsulamiento:
    print('En python no existen restricciones(se puede modificar de otra forma los atributos privados')
    coche1._Coche__color = 'Rojo2'  # MUY MALA PRACTICA
    coche1.conducir_coche()
