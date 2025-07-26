from Ejer_Sistemas_de_Libros.biblioteca import Biblioteca
from Ejer_Sistemas_de_Libros.libro import Libro

if __name__ == '__main__':
    bibliotecaCoderlan = Biblioteca('Biblioteca Coderland')

    # Agregar algunos libros
    libro1 = Libro('El alquimista', 'Paulo Cohelo', 'Ficcion')
    libro2 = Libro('1984', 'George Orwell', 'Ficcion')
    libro3 = Libro('El codigo Da Vincci', 'Dan Brown', 'Misterio')
    libro4 = Libro('Rayuela', 'Julio Cortázar', 'Ficcion')
    libro5 = Libro('Verónica decide morir', 'Paulo Cohelo', 'Ficcion')

    # Agregar los libros a la bibliotca

    bibliotecaCoderlan.agregar_libro(libro1)
    bibliotecaCoderlan.agregar_libro(libro2)
    bibliotecaCoderlan.agregar_libro(libro3)
    bibliotecaCoderlan.agregar_libro(libro4)
    bibliotecaCoderlan.agregar_libro(libro5)

    # Imprimimos el nombre de la biblioteca
    print(f'### Bienvenidos a la {bibliotecaCoderlan.nombre}')

    # Buscar Libros por autor
    print(f'\nLibros de Paulo Cohelo')
    bibliotecaCoderlan.buscar_libro_por_autor('Paulo Cohelo')

    # Buscar Libros por Genero
    print(f'\nLibros por Género')
    bibliotecaCoderlan.buscar_libro_por_genero('Ficcion')

    # Mostrar todos los libros de la biblioteca
    print(f'\Todos los libros de la Biblioteca')
    bibliotecaCoderlan.mostrar_todos_los_libros()
