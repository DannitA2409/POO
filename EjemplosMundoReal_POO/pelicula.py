class Pelicula:
    def __init__(self, titulo, precio_base):
        self._titulo = titulo  
        self._precio_base = precio_base

    def obtener_titulo(self):
        return self._titulo

    def calcular_precio(self):
        # Polimorfismo: este método se comportará distinto en las subclases
        return self._precio_base

class PeliculaRegular(Pelicula):
    def calcular_precio(self):
        return self._precio_base  # Precio normal

class Pelicula3D(Pelicula):
    def calcular_precio(self):
        # Polimorfismo: el 3D tiene un recargo del 20% y gafas
        return self._precio_base * 1.20