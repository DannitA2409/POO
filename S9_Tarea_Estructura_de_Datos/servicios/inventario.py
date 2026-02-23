import os
from modelos.producto import Producto

class Inventario:
    def __init__(self):
        self.archivo = "inventario.txt"
        self.lista_productos = []
        # Al iniciar la instancia, intenta cargar los datos automáticamente
        self.cargar_datos()

    def cargar_datos(self):
        """Lee el archivo de texto y reconstruye la lista de objetos."""
        if not os.path.exists(self.archivo):
            # Si el archivo no existe, lo crea vacío y sale
            try:
                open(self.archivo, 'w').close()
                print(f"[SISTEMA] Archivo '{self.archivo}' creado correctamente.")
            except PermissionError:
                print("[ERROR] No hay permisos para crear el archivo.")
            return

        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                lineas = f.readlines()
                self.lista_productos = []
                for linea in lineas:
                    # Limpia espacios y saltos de línea
                    linea = linea.strip()
                    if linea:
                        datos = linea.split(',')
                        # Valida que la línea tenga los 4 campos necesarios
                        if len(datos) == 4:
                            p = Producto(datos[0], datos[1], datos[2], datos[3])
                            self.lista_productos.append(p)
            print(f"[SISTEMA] Se cargaron {len(self.lista_productos)} productos desde el archivo.")

        except FileNotFoundError:
            print("[ERROR] El archivo no se encontró (se creará uno nuevo al guardar).")
        except PermissionError:
            print("[ERROR] Permiso denegado para leer el archivo.")
        except Exception as e:
            print(f"[ERROR] Ocurrió un error inesperado al leer: {e}")

    def guardar_datos(self):
        """Sobrescribe el archivo de texto con el estado actual de la lista."""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for prod in self.lista_productos:
                    f.write(prod.formato_archivo() + "\n")
            # print("[SISTEMA] Cambios guardados en archivo.")
            return True
        except PermissionError:
            print("[ERROR] No tiene permisos para escribir en el disco.")
            return False
        except Exception as e:
            print(f"[ERROR] No se pudo guardar el archivo: {e}")
            return False

    # --- Métodos CRUD modificados para invocar guardar_datos() ---

    def agregar_producto(self, producto):
        if self.buscar_por_id(producto.get_id()):
            return False, "El ID ya existe."
        
        self.lista_productos.append(producto)
        
        # Intenta guardar en disco inmediatamente
        if self.guardar_datos():
            return True, "Producto agregado y guardado en archivo."
        else:
            return True, "Producto agregado en memoria, pero FALLÓ al guardar en archivo."

    def eliminar_producto(self, id_prod):
        prod = self.buscar_por_id(id_prod)
        if prod:
            self.lista_productos.remove(prod)
            self.guardar_datos() # Guarda cambios
            return True
        return False

    def actualizar_producto(self, id_prod, cant=None, precio=None):
        prod = self.buscar_por_id(id_prod)
        if prod:
            if cant is not None: prod.set_cantidad(cant)
            if precio is not None: prod.set_precio(precio)
            self.guardar_datos() # Guarda cambios
            return True
        return False

    def buscar_por_id(self, id_prod):
        for p in self.lista_productos:
            if p.get_id() == id_prod:
                return p
        return None

    def listar_todos(self):
        return self.lista_productos