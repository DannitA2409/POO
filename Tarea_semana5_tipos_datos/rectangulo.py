from figura import Figura

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        super().__init__("Rectángulo")
        self.base = base      # Float
        self.altura = altura  # Float

    def calcular_area(self):
        """Implementación específica para el rectángulo"""
        self.resultado_area = self.base * self.altura
        self.esta_calculado = True
        return self.resultado_area