class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self._id = id_prod        
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_cantidad(self): return self._cantidad
    def set_cantidad(self, c): self._cantidad = c
    def get_precio(self): return self._precio
    def set_precio(self, p): self._precio = p

    # Este método será base para los hijos
    def to_dict(self):
        """Serializa el objeto a un diccionario para guardar en JSON"""
        return {
            "tipo": "generico",
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    def __str__(self):
        return f"ID: {self._id} | {self._nombre} | Cant: {self._cantidad} | ${self._precio}"