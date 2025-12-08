class Prestamo:
    def __init__(self, usuario, material):
        self._usuario = usuario
        self._material = material

    def realizar_prestamo(self):
        if self._material.prestar():
            return True
        return False

    def devolver_material(self):
        self._material.devolver()
