class Vehiculo:
    def __init__(self, marca: str, modelo: str, precio_base: float):
        self.__marca = marca           # Privado
        self.__modelo = modelo         # Privado
        self._precio_base = precio_base # Protegido (accesible por hijos)

    # Getters para acceder a los datos encapsulados
    def obtener_detalle(self):
        return f"{self.__marca} {self.__modelo}"

    def get_precio_base(self):
        return self._precio_base

    # POLIMORFISMO: Método que será sobrescrito por las clases hijas
    def calcular_impuesto(self):
        pass