from gestion.gestor_inventario import GestorInventario
from modelos.producto import Producto
from modelos.electronico import Electronico
from modelos.alimenticio import Alimenticio

def menu():
    gestor = GestorInventario()
    
    while True:
        print("\n=== SISTEMA AVANZADO DE INVENTARIO ===")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar por Nombre")
        print("5. Mostrar Todo")
        print("6. Salir")
        
        opcion = input(">>> Seleccione: ")

        if opcion == "1":
            try:
                tipo = input("Tipo (1: General, 2: Electrónico, 3: Alimento): ")
                id_p = input("ID Único: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))

                if tipo == "2":
                    gar = input("Meses de garantía: ")
                    prod = Electronico(id_p, nom, cant, pre, gar)
                elif tipo == "3":
                    ven = input("Fecha de vencimiento: ")
                    prod = Alimenticio(id_p, nom, cant, pre, ven)
                else:
                    prod = Producto(id_p, nom, cant, pre)

                gestor.agregar_producto(prod)
                print("¡Producto guardado exitosamente!")
            except ValueError as e:
                print(f"Error de validación: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            if gestor.eliminar_producto(id_p):
                print("Eliminado.")
            else:
                print("ID no encontrado.")

        elif opcion == "3":
            id_p = input("ID a actualizar: ")
            print("Deje en blanco si no desea modificar el campo.")
            n_cant = input("Nueva cantidad: ")
            n_prec = input("Nuevo precio: ")
            
            cant = int(n_cant) if n_cant else None
            prec = float(n_prec) if n_prec else None
            
            if gestor.actualizar_producto(id_p, cant, prec):
                print("Actualizado.")
            else:
                print("No se encontró el producto.")

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            res = gestor.buscar_por_nombre(nom)
            if res:
                for p in res:
                    print(p)
            else:
                print("No hay coincidencias.")

        elif opcion == "5":
            items = gestor.listar_todos()
            print(f"\n--- Total ítems: {len(items)} ---")
            for p in items:
                print(p)

        elif opcion == "6":
            print("Saliendo...")
            break

if __name__ == "__main__":
    menu()