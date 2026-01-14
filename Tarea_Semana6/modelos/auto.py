# modelos/auto.py
from modelos.vehiculo import Vehiculo

# HERENCIA: Auto hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio_base, puertas):
        super().__init__(marca, modelo, precio_base)
        self.puertas = puertas

    # POLIMORFISMO: Sobrescribimos el método para un cálculo específico
    def calcular_impuesto(self):
        # El impuesto de un auto es el 10% del precio base
        return self._precio_base * 0.10

    def __str__(self):
        return f"Auto: {self.obtener_detalle()} | Puertas: {self.puertas}"