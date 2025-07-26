class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')


class Perro(Animal):
    def ladrar(self):
        print('Puedo ladrar')

    # sobreescribiendo el metodo heredado de la case padre
    def dormir(self):
        print('Duermo 15 horas al dia')


# Programa principal
if __name__ == '__main__':
    print('---Soy un animal---')
    animal1 = Animal()
    animal1.comer()
    animal1.dormir()

    print('\n Clase Hija: Soy un perro')
    perro = Perro()
    perro.comer()
    perro.ladrar()
    perro.dormir()
