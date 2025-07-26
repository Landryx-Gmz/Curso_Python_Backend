class Animal:
    def hacer_sonido(self):
        print('hago un sonido')


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')


class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')


class Gata(Gato):
    pass


print('### Ejemplo de polimorfismo###')
print('Calse padre Animal:')
animal1 = Animal()
animal1.hacer_sonido()

print('\nClase Hijo Perro')
perro1 = Perro()
perro1.hacer_sonido()

print('\nClase Hija Gato')
gato1 = Gato()
gato1.hacer_sonido()

print('\nClase hija Gata')
gata1 = Gata()
gata1.hacer_sonido()
