"""
Sistema de Gestión de Inventarios
Descripción: Sistema modular para gestionar productos usando listas y objetos.
"""

from modelos.producto import Producto
from servicios.inventario import Inventario
import os

def limpiar_pantalla():
    """Función auxiliar para limpiar la consola según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    # Instancia la clase de servicio
    inventario = Inventario()

    while True:
        print("\n========================================")
        print("   SISTEMA DE GESTIÓN DE INVENTARIOS")
        print("========================================")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto (Cantidad/Precio)")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        
        opcion = input(">>> Seleccione una opción: ")

        if opcion == "1":
            print("\n--- AÑADIR PRODUCTO ---")
            id_p = input("Ingrese ID único: ")
            nombre = input("Ingrese nombre: ")
            try:
                # Valida que cantidad y precio sean números
                cant = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                
                # Creas el objeto Producto
                nuevo_prod = Producto(id_p, nombre, cant, precio)
                
                # Llama al servicio para guardar
                if inventario.agregar_producto(nuevo_prod):
                    print("¡Producto agregado exitosamente!")
                else:
                    print("Error: Ya existe un producto con ese ID.")
            except ValueError:
                print("Error: La cantidad debe ser entero y el precio decimal.")

        elif opcion == "2":
            print("\n--- ELIMINAR PRODUCTO ---")
            id_p = input("Ingrese el ID del producto a eliminar: ")
            if inventario.eliminar_producto(id_p):
                print("Producto eliminado correctamente.")
            else:
                print("Error: No se encontró un producto con ese ID.")

        elif opcion == "3":
            print("\n--- ACTUALIZAR PRODUCTO ---")
            id_p = input("Ingrese el ID del producto a actualizar: ")
            
            # Verifica si existe antes de pedir datos
            if inventario.buscar_por_id(id_p):
                try:
                    nueva_cant = int(input("Nueva cantidad: "))
                    nuevo_precio = float(input("Nuevo precio: "))
                    inventario.actualizar_producto(id_p, nueva_cant, nuevo_precio)
                    print("Producto actualizado correctamente.")
                except ValueError:
                    print("Error: Ingrese valores numéricos válidos.")
            else:
                print("Error: Producto no encontrado.")

        elif opcion == "4":
            print("\n--- BUSCAR PRODUCTO ---")
            termino = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(termino)
            if resultados:
                print(f"Se encontraron {len(resultados)} coincidencias:")
                for p in resultados:
                    print(p) # Llama automáticamente al método __str__
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            print("\n--- LISTA DE INVENTARIO ---")
            productos = inventario.listar_todos()
            if productos:
                for p in productos:
                    print(p)
            else:
                print("El inventario está vacío.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    menu_principal()