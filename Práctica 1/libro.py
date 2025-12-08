from material import Material

class Libro(Material):
    def __init__(self, titulo, codigo, autor):
        super().__init__(titulo, codigo)
        self._autor = autor

    def mostrar_info(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"Libro | {self._codigo} - {self._titulo} | Autor: {self._autor} | {estado}"
