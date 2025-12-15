class DatosDiarios:
    """
    Clase Padre.
    Maneja la estructura básica de almacenamiento de datos.
    Aplica ENCAPSULAMIENTO.
    """
    def __init__(self):
        # Atributo privado (__datos) para que no se modifique externamente
        self.__datos = []

    def agregar_dato(self, dato):
        """Método público para insertar datos de forma segura."""
        self.__datos.append(dato)

    def _obtener_datos(self):
        """
        Método protegido.
        Permite que las clases hijas accedan a los datos, 
        manteniendo el encapsulamiento hacia el exterior.
        """
        return self.__datos

    def calcular_promedio(self):
        """
        Método base vacío. Se espera que las clases hijas lo implementen
        """