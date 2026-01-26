class SesionUsuario:
    def __init__(self, usuario: str, nivel_acceso: str = "Básico"):
        """
        CONSTRUCTOR (__init__):
        - Inicializa los datos obligatorios del usuario.
        - Asigna valores por defecto (nivel_acceso).
        - Simula el inicio de una conexión al servidor.
        """
        self.usuario = usuario
        self.nivel_acceso = nivel_acceso
        self.token_activa = True  # Atributo que representa el estado
        
        print(f"\n[CONSTRUCTOR]: Sesión INICIADA para el usuario '{self.usuario}'.")
        print(f"               Nivel asignado: {self.nivel_acceso}.")

    def ejecutar_accion(self, accion: str):
        """Simula una actividad del usuario en el sistema"""
        if self.token_activa:
            print(f"[SESIÓN]: Usuario {self.usuario} está realizando: {accion}")

    def __del__(self):
        """
        DESTRUCTOR (__del__):
        - Limpieza: Cambia el estado del token a False y libera el 'slot' del servidor.
        - Se ejecuta cuando el objeto se elimina con 'del' o se sobrescribe.
        - Garantiza que no queden sesiones "fantasma" en memoria.
        """
        self.token_activa = False
        print(f"\n[DESTRUCTOR]: Sesión CERRADA para '{self.usuario}'.")
        print(f"              Limpieza: Espacio en servidor liberado correctamente.")