class Sala:
    def __init__(self, numero, capacidad):
        self.__numero = numero
        self.__capacidad = capacidad
        self.__ocupados = 0  # Atributo privado

    def hay_espacio(self, cantidad):
        return (self.__ocupados + cantidad) <= self.__capacidad

    def ocupar_asientos(self, cantidad):
        if self.hay_espacio(cantidad):
            self.__ocupados += cantidad
            return True
        return False

    def obtener_info(self):
        return f"Sala {self.__numero} (Disponibles: {self.__capacidad - self.__ocupados})"