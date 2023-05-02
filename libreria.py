from typing import List


class NoDisponible(Exception):
    pass

class NoSeHaPrestado(Exception):
    pass

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if(not self.disponible):
            raise NoDisponible('El libro no está disponible')
        self.disponible = False


    def devolver(self):
        if(self.disponible):
            raise NoSeHaPrestado('El libro no se ha prestado previamente')
        self.disponible = True

    
    def mostrar_informacion(self):
        print(f'Título: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nEstado de disponibilidad: {self.disponible}')


class Biblioteca:

    def __init__(self):
        self.libros : List[Libro] = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    def prestar_libro(self, isbn: str):
        for libro in self.libros:
            if(libro.isbn == isbn):
                libro.prestar()
    
    def devolver_libro(self, isbn:str):
        for libro in self.libros:
            if(libro.isbn == isbn):
                libro.devolver()

    def mostrar_libros(self):
        print('*********** LIBROS DE LA BIBLIOTECA ***********')
        print('----------------------------------------------------------')
        for libro in self.libros:
            libro.mostrar_informacion()
            print('----------------------------------------------------------')

biblioteca = Biblioteca()
biblioteca.agregar_libro(Libro('Las Valkirias', 'Paulo Coelho', '1', True))
biblioteca.agregar_libro(Libro('Veronika decide morir', 'Paulo Coelho', '2', True))
biblioteca.agregar_libro(Libro('100 Años de soledad', 'Gabo', '3', True))
biblioteca.mostrar_libros()
try:
    biblioteca.prestar_libro('1')
    biblioteca.mostrar_libros()
    biblioteca.devolver_libro('1')
    biblioteca.mostrar_libros()
    biblioteca.devolver_libro('2')
except Exception as e:
    print('Se produjo el siguiente error: ', e)
# libro = Libro('Las Valkirias', 'Paulo Coelho', '3131', True)
# libro.mostrar_informacion()
# try:
#     libro.prestar()
#     libro.mostrar_informacion()
#     libro.devolver()
#     libro.mostrar_informacion()
# except Exception as e:
#     print('Se produjo el siguiente error: ', e)
#     libro.mostrar_informacion()




