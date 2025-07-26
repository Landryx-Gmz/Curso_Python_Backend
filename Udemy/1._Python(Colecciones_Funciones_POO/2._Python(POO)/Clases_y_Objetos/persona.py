# Definir de la clase

class Persona:

    # Constructor __init__ (dunder - double uderscore)

    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_contacto(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Direcion en memoria self: {id(self)}')
        print(f'Direcion en memoria  hexadecima self: {hex(id(self))}')


# Creacion de objetos en programa principla
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Andy', 'Gomez')
    persona1.mostrar_contacto()

    # Creacion de segundo objeto
    persona2 = Persona('Rosa',
                       'Montoya')  # Mediante una variable llamamos a la clase constructor y pasamos directamente los atributos de la nueva clase creada.
    persona2.mostrar_contacto()  # Llamamos al metodo para imprimir sus datos
