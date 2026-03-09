class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        # ENCAPSULAMIENTO: Atributos privados
        self.__isbn = isbn
        # COLECCIÓN (Tupla): Almacena título y autor como una tupla inmutable
        self.__info_basica = (titulo, autor)
        self.__categoria = categoria

    # Getters para acceder de forma segura a los atributos privados
    @property
    def isbn(self):
        return self.__isbn

    @property
    def titulo(self):
        return self.__info_basica[0] # Accede al primer elemento de la tupla

    @property
    def autor(self):
        return self.__info_basica[1] # Accede al segundo elemento de la tupla

    @property
    def categoria(self):
        return self.__categoria

    def __str__(self):
        return f"ISBN: {self.__isbn} | '{self.titulo}' por {self.autor} (Cat: {self.__categoria})"