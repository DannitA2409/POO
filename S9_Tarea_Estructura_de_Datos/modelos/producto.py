class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa los atributos privados para garantizar el encapsulamiento.
        """
        self.__id = id_prod          # Identificador único
        self.__nombre = nombre       # Nombre del producto
        self.__cantidad = cantidad   # Stock disponible (int)
        self.__precio = precio       # Costo unitario (float)

    # --- GETTERS ---
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # --- SETTERS ---
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cant: {self.__cantidad} | Precio: ${self.__precio:.2f}"