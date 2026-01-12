"""Representa una figura geométrica general"""
class Figura:
    def __init__(self, nombre: str):
        # Atributos con diferentes tipos de datos
        self.nombre_figura = nombre  # String
        self.esta_calculado = False   # Boolean
        self.resultado_area = 0.0     # Float

    def calcular_area(self):
        """Método que será sobrescrito por las clases hijas"""
        pass

    def mostrar_info(self):
        """Muestra la información básica de la figura"""
        estado = "Calculado" if self.esta_calculado else "No calculado"
        print(f"\n--- Figura: {self.nombre_figura} ---")
        print(f"Estado: {estado}")
        if self.esta_calculado:
            print(f"Área resultante: {self.resultado_area:.2f} unidades cuadradas")