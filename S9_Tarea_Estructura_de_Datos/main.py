"""
Sistema de Gestión de Inventarios
Descripción: Sistema modular para gestionar productos usando listas y objetos.
"""

import os
from modelos.producto import Producto
from servicios.inventario import Inventario

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    # Al instanciar, automáticamente carga el archivo gracias al __init__
    sistema = Inventario()

    while True:
        print("\n=== GESTIÓN DE INVENTARIO CON ARCHIVOS ===")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Ver Inventario Completo")
        print("5. Salir")
        
        opc = input(">>> Opción: ")

        if opc == "1":
            try:
                id_p = input("ID: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                
                nuevo = Producto(id_p, nom, cant, pre)
                
                # El método ahora retorna una tupla (Exito, Mensaje)
                exito, mensaje = sistema.agregar_producto(nuevo)
                print(f"Resultado: {mensaje}")
                
            except ValueError:
                print("Error: Los datos numéricos no son válidos.")

        elif opc == "2":
            id_p = input("ID a eliminar: ")
            if sistema.eliminar_producto(id_p):
                print("Eliminado y cambios guardados en disco.")
            else:
                print("Producto no encontrado.")

        elif opc == "3":
            id_p = input("ID a actualizar: ")
            prod = sistema.buscar_por_id(id_p)
            if prod:
                print(f"Editando: {prod.get_nombre()}")
                try:
                    nc = int(input("Nueva cantidad: "))
                    np = float(input("Nuevo precio: "))
                    sistema.actualizar_producto(id_p, nc, np)
                    print("Actualizado y cambios guardados en disco.")
                except ValueError:
                    print("Error: Ingrese números válidos.")
            else:
                print("Producto no encontrado.")

        elif opc == "4":
            lista = sistema.listar_todos()
            print(f"\n--- LISTADO ({len(lista)} productos) ---")
            if not lista:
                print("(Inventario vacío o error de lectura)")
            for p in lista:
                print(p)

        elif opc == "5":
            print("Saliendo... (Los datos ya están seguros en el archivo)")
            break
        
        else:
            print("Opción inválida.")
        
        input("[Enter para continuar]")
        limpiar()

if __name__ == "__main__":
    menu()