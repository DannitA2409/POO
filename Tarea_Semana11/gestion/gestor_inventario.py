import json
import os
from modelos.producto import Producto
from modelos.electronico import Electronico
from modelos.alimenticio import Alimenticio

class GestorInventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        # COLECCIÓN PRINCIPAL: Diccionario { id : ObjetoProducto }
        # Usa un diccionario para acceso rápido por clave (ID)
        self.productos = {} 
        self.cargar_inventario()

    def agregar_producto(self, producto):
        """Añade un producto al diccionario y guarda en disco"""
        if producto.get_id() in self.productos:
            raise ValueError("El ID ya existe en el inventario.")
        
        # Guarda en la colección en memoria
        self.productos[producto.get_id()] = producto
        self.guardar_inventario()

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            del self.productos[id_prod] # Elimina del diccionario
            self.guardar_inventario()
            return True
        return False

    def actualizar_producto(self, id_prod, cantidad=None, precio=None):
        if id_prod in self.productos:
            prod = self.productos[id_prod]
            if cantidad is not None: prod.set_cantidad(cantidad)
            if precio is not None: prod.set_precio(precio)
            self.guardar_inventario()
            return True
        return False

    def buscar_por_nombre(self, nombre):
        """
        Retorna una LISTA de productos que coincidan.
        Aquí convierte los valores del diccionario a una lista para iterar.
        """
        resultados = []
        for prod in self.productos.values():
            if nombre.lower() in prod.get_nombre().lower():
                resultados.append(prod)
        return resultados

    def listar_todos(self):
        # Retorna los valores del diccionario (los objetos)
        return list(self.productos.values())

    # PERSISTENCIA

    def guardar_inventario(self):
        """Convierte objetos a diccionarios y guarda en JSON"""
        try:
            data = {}
            for id_p, prod in self.productos.items():
                data[id_p] = prod.to_dict() 
            
            with open(self.archivo, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error al guardar archivo: {e}")

    def cargar_inventario(self):
        """Lee JSON y reconstruye los objetos"""
        if not os.path.exists(self.archivo):
            return

        try:
            with open(self.archivo, 'r') as f:
                data = json.load(f)
                
            self.productos = {}
            for id_p, info in data.items():
                # Fábrica simple para instanciar según el tipo
                tipo = info.get("tipo")
                
                if tipo == "electronico":
                    p = Electronico(info["id"], info["nombre"], info["cantidad"], info["precio"], info["garantia"])
                elif tipo == "alimenticio":
                    p = Alimenticio(info["id"], info["nombre"], info["cantidad"], info["precio"], info["vencimiento"])
                else:
                    p = Producto(info["id"], info["nombre"], info["cantidad"], info["precio"])
                
                self.productos[id_p] = p
        except Exception as e:
            print(f"Error al cargar archivo (posible corrupción): {e}")