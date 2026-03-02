from modelos.producto import Producto

class Electronico(Producto):
    def __init__(self, id_prod, nombre, cantidad, precio, garantia):
        # Llama al constructor del padre
        super().__init__(id_prod, nombre, cantidad, precio)
        self._garantia = garantia # Atributo exclusivo

    # Sobrescribe to_dict
    def to_dict(self):
        data = super().to_dict() # Reutiliza la lógica del padre
        data["tipo"] = "electronico"
        data["garantia"] = self._garantia
        return data

    def __str__(self):
        return super().__str__() + f" | Garantía: {self._garantia} meses"