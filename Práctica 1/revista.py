from material import Material

class Revista(Material):
    def __init__(self, titulo, codigo, numero):
        super().__init__(titulo, codigo)
        self._numero = numero

    def mostrar_info(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"Revista | {self._codigo} - {self._titulo} | Nro: {self._numero} | {estado}"