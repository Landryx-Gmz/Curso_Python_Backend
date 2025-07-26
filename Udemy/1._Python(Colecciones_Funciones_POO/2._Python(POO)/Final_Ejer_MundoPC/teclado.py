from Final_Ejer_MundoPC.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contadro_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contadro_teclado += 1
        self.id_teclado = Teclado.contadro_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self.id_teclado}, Marca: {self.marca}, Tipo_entrada: {self.tipo_entrada}'


if __name__ == '__main__':
    teclado1 = Teclado('Acer', 'Cable')
    print(teclado1)

    teclado2 = Teclado('Asus', 'USB')
    print(teclado2)
