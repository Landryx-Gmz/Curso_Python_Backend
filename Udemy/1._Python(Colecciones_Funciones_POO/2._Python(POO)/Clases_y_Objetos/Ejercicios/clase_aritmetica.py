class Aritmetica:
    # Constructor
    def __init__(self, operando1: int, operando2: int):
        # Atributos
        self.operando1 = operando1
        self.operando2 = operando2

    # Metodos
    def mostrar_operandos(self):
        return f'{self.operando1} y {self.operando2}'

    def sumar(self):
        suma = self.operando1 + self.operando2
        print(f'''La suma de {self.mostrar_operandos()} es: {suma}''')

    def restar(self):
        resta = self.operando1 - self.operando2
        print(f'La resta de {self.mostrar_operandos()} es: {resta}')

    def multiplicar(self):
        multiplicar = self.operando1 * self.operando2
        print(f'La multiplicacion de {self.mostrar_operandos()} es: {multiplicar}')

    def dividir(self):
        if self.operando2 == 0:
            print('No se puede dividir por cero')
            return
        dividir = self.operando1 / self.operando2
        print(f'La división de {self.mostrar_operandos()} es: {dividir}')


# Principal
if __name__ == '__main__':
    aritmetica1 = Aritmetica(2, 2)  # Creacion mediante el constructor
    aritmetica1.sumar()  # Llamada de metodo de clase

    aritmetica2 = Aritmetica(5, 2)
    aritmetica2.restar()

    aritmetica3 = Aritmetica(5, 6)
    aritmetica3.multiplicar()

    aritmetica4 = Aritmetica(3, 0)
    aritmetica4.dividir()

    # Crear objetos y luego asignar sus atributos
    # Ojo esto es mala practica

    '''aritmetica5 = Aritmetica()
    aritmetica5.operando1 = 4
    aritmetica5.operando2 = 4
    aritmetica5.multiplicar()'''

# Da error porque para que funcione tiene que el constructor tener asignado el  valor de None en sus parametros: def __init__(self, operando1=None, operando2=None): NO ES RECOMENDABLE
