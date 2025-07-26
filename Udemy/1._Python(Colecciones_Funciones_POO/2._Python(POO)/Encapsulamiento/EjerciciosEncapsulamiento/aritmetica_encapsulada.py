class Aritmetica:
    # Constructor
    def __init__(self, operando1: int, operando2: int):
        # Atributos
        self._operando1 = operando1
        self._operando2 = operando2

    def get_operando1(self):
        return self._operando1

    def set_operando1(self, operando_1):
        self._operando1 = operando_1

    def get_operando2(self):
        return self._operando2

    def set_operando2(self, operando_2):
        self._operando2 = operando_2

    # Metodos
    def mostrar_operandos(self):
        return f'{self.get_operando1()} y {self.get_operando2()}'

    def sumar(self):
        suma = self._operando1 + self._operando2
        print(f'La suma de {self.mostrar_operandos()} es: {suma}\n')

    def restar(self):
        resta = self._operando1 - self._operando2
        print(f'La resta de {self.mostrar_operandos()} es: {resta}\n')

    def multiplicar(self):
        multiplicar = self._operando1 * self._operando2
        print(f'La multiplicacion de {self.mostrar_operandos()} es: {multiplicar}\n')

    def dividir(self):
        if self._operando2 == 0:
            print('No se puede dividir por cero')
            return
        dividir = self._operando1 / self._operando2
        print(f'La división de {self.mostrar_operandos()} es: {dividir}\n')


# Principal
if __name__ == '__main__':
    aritmetica1 = Aritmetica(2, 2)  # Creacion mediante el constructor
    aritmetica1.sumar()  # Llamada de metodo de clase

    print(f'Utilizamos el setter para la suma')
    aritmetica1.set_operando1(3)
    aritmetica1.set_operando2(3)
    aritmetica1.sumar()

    aritmetica2 = Aritmetica(5, 2)
    aritmetica2.restar()

    print(f'Utilizamos el setter para la suma')
    aritmetica2.set_operando1(6)
    aritmetica2.set_operando2(45)
    aritmetica2.restar()

    aritmetica3 = Aritmetica(5, 6)
    aritmetica3.multiplicar()

    aritmetica4 = Aritmetica(3, 0)
    aritmetica4.dividir()
