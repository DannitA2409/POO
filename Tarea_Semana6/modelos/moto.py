# modelos/moto.py
from modelos.vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio_base, cilindrada):
        super().__init__(marca, modelo, precio_base)
        self.cilindrada = cilindrada

    # POLIMORFISMO: Las motos pagan menos impuesto (5%)
    def calcular_impuesto(self):
        return self._precio_base * 0.05

    def __str__(self):
        return f"Moto: {self.obtener_detalle()} | Cilindrada: {self.cilindrada}cc"