from modelos.producto import Producto

class Inventario:
    def __init__(self):
        """
        Constructor del Inventario.
        Inicializa una lista vacía donde se almacenarán los objetos Producto.
        """
        self.lista_productos = []

    def agregar_producto(self, producto):
        """
        Verifica que el ID sea único antes de agregar.
        Retorna True si se agregó, False si el ID ya existe.
        """
        # Valida unicidad del ID
        if self.buscar_por_id(producto.get_id()):
            return False
        
        self.lista_productos.append(producto)
        return True

    def eliminar_producto(self, id_prod):
        """
        Busca un producto por ID y lo elimina de la lista.
        Retorna True si se eliminó, False si no se encontró.
        """
        prod = self.buscar_por_id(id_prod)
        if prod:
            self.lista_productos.remove(prod)
            return True
        return False

    def actualizar_producto(self, id_prod, nueva_cantidad=None, nuevo_precio=None):
        """
        Busca un producto y actualiza sus valores si se proporcionan.
        """
        prod = self.buscar_por_id(id_prod)
        if prod:
            if nueva_cantidad is not None:
                prod.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                prod.set_precio(nuevo_precio)
            return True
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos que contengan la cadena 'nombre' (coincidencia parcial).
        Retorna una lista de coincidencias.
        """
        resultados = []
        for p in self.lista_productos:
            # Convierte a minúsculas para que la búsqueda no distinga mayúsculas
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def buscar_por_id(self, id_prod):
        """Método auxiliar privado para buscar un objeto por su ID exacto"""
        for p in self.lista_productos:
            if p.get_id() == id_prod:
                return p
        return None

    def listar_todos(self):
        """Retorna la lista completa de productos"""
        return self.lista_productos