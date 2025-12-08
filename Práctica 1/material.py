class Material:
    def __init__(self, titulo, codigo):
        self._titulo = titulo
        self._codigo = codigo
        self._disponible = True

    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def devolver(self):
        self._disponible = True

    def esta_disponible(self):
        return self._disponible

    def mostrar_info(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"{self._codigo} - {self._titulo} ({estado})"
