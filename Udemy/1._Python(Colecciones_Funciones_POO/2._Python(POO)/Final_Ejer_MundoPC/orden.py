class Orden:
    contador_orden = 0

    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self.id_ordenes = Orden.contador_orden
        # Recibimos la lista de tipo computadora
        self.computadoras = computadoras

    def agragar_computador(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()

        return f'''--ORDEN {self.id_ordenes}
        Computadoras: {computadoras_str}'''
