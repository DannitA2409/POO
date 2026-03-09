import os
from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    servicio = BibliotecaServicio()

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL ===")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados de un usuario")
        print("9. Salir")
        
        opc = input("Seleccione una opción: ")

        if opc == "1":
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            exito, msj = servicio.añadir_libro(libro)
            print(f"> {msj}")

        elif opc == "2":
            isbn = input("ISBN del libro a eliminar: ")
            exito, msj = servicio.quitar_libro(isbn)
            print(f"> {msj}")

        elif opc == "3":
            id_u = input("ID de Usuario: ")
            nombre = input("Nombre: ")
            usuario = Usuario(id_u, nombre)
            exito, msj = servicio.registrar_usuario(usuario)
            print(f"> {msj}")

        elif opc == "4":
            id_u = input("ID de Usuario a dar de baja: ")
            exito, msj = servicio.dar_baja_usuario(id_u)
            print(f"> {msj}")

        elif opc == "5":
            isbn = input("ISBN del libro a prestar: ")
            id_u = input("ID del Usuario: ")
            exito, msj = servicio.prestar_libro(isbn, id_u)
            print(f"> {msj}")

        elif opc == "6":
            isbn = input("ISBN del libro a devolver: ")
            id_u = input("ID del Usuario: ")
            exito, msj = servicio.devolver_libro(isbn, id_u)
            print(f"> {msj}")

        elif opc == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            if criterio in ['titulo', 'autor', 'categoria']:
                valor = input(f"Ingrese el valor para {criterio}: ")
                resultados = servicio.buscar_libro(criterio, valor)
                if resultados:
                    print("\n--- Resultados ---")
                    for r in resultados: print(r)
                else:
                    print("> No se encontraron libros disponibles.")
            else:
                print("> Criterio inválido.")

        elif opc == "8":
            id_u = input("ID del Usuario: ")
            prestados = servicio.listar_prestados(id_u)
            if prestados is not None:
                print(f"\n--- Libros prestados (Total: {len(prestados)}) ---")
                for libro in prestados: print(libro)
            else:
                print("> Usuario no encontrado.")

        elif opc == "9":
            print("Saliendo del sistema...")
            break
        
        else:
            print("Opción inválida.")
            
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()