"""
Proyecto: Gestión de Concesionaria
Conceptos POO aplicados:
1. Herencia: Auto y Moto heredan de Vehiculo.
2. Encapsulamiento: Atributos privados (__marca, __modelo) en Vehiculo.
3. Polimorfismo: Diferente implementación de calcular_impuesto().
4. Abstracción: Separación en carpetas de modelos y servicios.
"""

from modelos.auto import Auto
from modelos.moto import Moto
from servicios.gestion_inventario import GestionInventario

def menu():
    sistema = GestionInventario()
    
    while True:
        print("\n--- MENÚ CONCESIONARIA ---")
        print("1. Registrar Auto")
        print("2. Registrar Moto")
        print("3. Ver Inventario y Reporte")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            m = input("Marca: ")
            mod = input("Modelo: ")
            p = float(input("Precio Base: "))
            puertas = int(input("Número de puertas: "))
            nuevo_auto = Auto(m, mod, p, puertas)
            sistema.agregar_vehiculo(nuevo_auto)

        elif opcion == "2":
            m = input("Marca: ")
            mod = input("Modelo: ")
            p = float(input("Precio Base: "))
            c = int(input("Cilindrada (cc): "))
            nueva_moto = Moto(m, mod, p, c)
            sistema.agregar_vehiculo(nueva_moto)

        elif opcion == "3":
            sistema.mostrar_reporte()

        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()