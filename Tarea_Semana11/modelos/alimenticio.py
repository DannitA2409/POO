from modelos.producto import Producto

class Alimenticio(Producto):
    def __init__(self, id_prod, nombre, cantidad, precio, fecha_vencimiento):
        super().__init__(id_prod, nombre, cantidad, precio)
        self._fecha_vencimiento = fecha_vencimiento

    # Sobrescribe to_dict
    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "alimenticio"
        data["vencimiento"] = self._fecha_vencimiento
        return data

    def __str__(self):
        return super().__str__() + f" | Vence: {self._fecha_vencimiento}"