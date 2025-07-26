class Persona:
    # Atributo o metodo  de clase
    contador_persona = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    # Primera forma o manera de accder a atributo estatico
    @staticmethod
    def get_contador_personas_estatico():
        print('Metdod estatico')
        return Persona.contador_persona

    # Segunda forma o manera de accder a atributo estatico
    @classmethod
    def get_condaro_personas_clase(cls):  # class
        print(f'Metodo de clase')
        return cls.contador_persona  # se lee: regresa el contador persona de la clase(cls)

    # Programa Principal


if __name__ == '__main__':
    print('*** Ejemplo contador de Objetos***')
    persona1 = Persona('Andy', 'Gomez')
    persona1.mostrar_persona()
    persona2 = Persona('Rosa', 'Montoya')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contado de objetos persona: {Persona.contador_persona}')
    # Imprimir el metodo persona con @staticmethod
    print(f'Contador objetos Persona(static): {Persona.get_contador_personas_estatico()} ')
    # Imprimir el metod persona con @classmethod (cls)
    print(f'Contador objetos Persona(cls): {Persona.get_condaro_personas_clase()}')
