class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apelllido = apellido

    # Sobreescribie el metodo __str__
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apelllido}
        Dir. Mem. = {super.__str__(self)}'''

    # Codigo Principal


if __name__ == '__main__':
    persona1 = Persona('Andy', 'Gomez')
    print(persona1)  # El metodo str se llama automaticamente desde el print()
