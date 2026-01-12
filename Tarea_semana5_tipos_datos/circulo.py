import math
from figura import Figura

class Circulo(Figura):
    def __init__(self, radio: float):
        # Llama al constructor de la clase padre
        super().__init__("Círculo")
        self.radio = radio  # Float

    def calcular_area(self):
        """Implementación específica para el círculo"""
        self.resultado_area = math.pi * (self.radio ** 2)
        self.esta_calculado = True
        return self.resultado_area