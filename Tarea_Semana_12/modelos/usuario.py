class Usuario:
    def __init__(self, id_usuario, nombre):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        # COLECCIÓN (Lista): Permite almacenar objetos Libro de forma dinámica
        self.__libros_prestados =[]

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def nombre(self):
        return self.__nombre

    @property
    def libros_prestados(self):
        return self.__libros_prestados

    def prestar_libro(self, libro):
        """Añade un libro a la lista de préstamos del usuario"""
        self.__libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        """Busca el libro por ISBN en la lista, lo elimina de la lista y lo retorna"""
        for libro in self.__libros_prestados:
            if libro.isbn == isbn:
                self.__libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self.__nombre} (ID: {self.__id_usuario}) - Préstamos activos: {len(self.__libros_prestados)}"