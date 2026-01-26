from servicios.administrador import AdministradorSesiones

def mostrar_menu():
    print("\n--- MENÚ DE SERVIDOR ---")
    print("1. Iniciar Sesión de Usuario")
    print("2. Realizar Tarea en el Sistema")
    print("3. Cerrar Sesión Actual (Eliminar objeto)")
    print("4. Salir del Programa")
    return input("Seleccione una opción: ")

def ejecutar():
    admin = AdministradorSesiones()
    
    while True:
        opc = mostrar_menu()
        
        if opc == "1":
            nombre = input("Ingrese nombre de usuario: ")
            nivel = input("Ingrese nivel (Admin/Básico): ")
            # Si ya había alguien logueado, se activa el __del__ 
            # del usuario anterior automáticamente al crear el nuevo.
            admin.abrir_sesion(nombre, nivel)
            
        elif opc == "2":
            tarea = input("¿Qué tarea desea realizar?: ")
            admin.realizar_tarea(tarea)
            
        elif opc == "3":
            admin.cerrar_sesion_manual()
            
        elif opc == "4":
            print("Finalizando programa. Todas las sesiones restantes se cerrarán.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    ejecutar()
    # Al terminar el programa aquí, si quedaba una sesión abierta, 
    # Python llama al destructor final.