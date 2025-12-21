from pelicula import PeliculaRegular, Pelicula3D
from gestion_cine import Cine

def menu():
    mi_cine = Cine()
    # Carga algunos datos iniciales
    mi_cine.agregar_pelicula(PeliculaRegular("Avatar 2", 5.0))
    mi_cine.agregar_pelicula(Pelicula3D("Avatar 2 (3D)", 5.0))
    mi_cine.agregar_pelicula(PeliculaRegular("Kung Fu Panda", 4.0))

    while True:
        print("\n===== SISTEMA DE CINE =====")
        print("1. Ver cartelera")
        print("2. Comprar entradas")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mi_cine.mostrar_cartelera()
        
        elif opcion == "2":
            mi_cine.mostrar_cartelera()
            peli_idx = int(input("Número de película: ")) - 1
            cantidad = int(input("¿Cuántas personas?: "))
            mi_cine.realizar_venta(peli_idx, cantidad)
            
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()