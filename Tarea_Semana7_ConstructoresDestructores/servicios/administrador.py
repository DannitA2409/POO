from modelos.sesion import SesionUsuario

class AdministradorSesiones:
    def __init__(self):
        # El administrador empieza sin ninguna sesión activa
        self.sesion_actual = None

    def abrir_sesion(self, nombre, nivel):
        
        print(f"\n--- Intentando abrir sesión para {nombre} ---")
        self.sesion_actual = SesionUsuario(nombre, nivel)

    def realizar_tarea(self, tarea):
        if self.sesion_actual:
            self.sesion_actual.ejecutar_accion(tarea)
        else:
            print("Error: No hay ninguna sesión activa en el sistema.")

    def cerrar_sesion_manual(self):
        if self.sesion_actual:
            print(f"Cerrando sesión de {self.sesion_actual.usuario} por solicitud...")
            # Al hacer la variable None, el objeto pierde su referencia y muere
            self.sesion_actual = None
        else:
            print("No hay sesiones para cerrar.")