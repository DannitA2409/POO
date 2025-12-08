class Usuario:
    def __init__(self, nombre, cedula):
        self._nombre = nombre
        self._cedula = cedula

    def mostrar_info(self):
        return f"{self._nombre} - CI: {self._cedula}"
