from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    def __init__(self):
        # COLECCIÓN (Diccionario): Clave=ISBN, Valor=Objeto Libro
        self.__libros_disponibles = {}
        
        # COLECCIÓN (Diccionario): Clave=ID, Valor=Objeto Usuario
        self.__usuarios = {}
        
        # COLECCIÓN (Conjunto/Set): Almacena solo los IDs para validar unicidad rápidamente
        self.__ids_usuarios = set()

    # GESTIÓN DE LIBROS
    def añadir_libro(self, libro):
        if libro.isbn in self.__libros_disponibles:
            return False, "El ISBN ya está registrado."
        self.__libros_disponibles[libro.isbn] = libro
        return True, "Libro añadido con éxito."

    def quitar_libro(self, isbn):
        if isbn in self.__libros_disponibles:
            del self.__libros_disponibles[isbn]
            return True, "Libro eliminado del catálogo."
        return False, "Libro no encontrado o actualmente prestado."

    def buscar_libro(self, criterio, valor):
        """Busca en el diccionario de libros disponibles según título, autor o categoría"""
        resultados =[]
        valor = valor.lower()
        for libro in self.__libros_disponibles.values():
            if criterio == "titulo" and valor in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # GESTIÓN DE USUARIOS
    def registrar_usuario(self, usuario):
        # Usa el conjunto (Set) para una validación rápida
        if usuario.id_usuario in self.__ids_usuarios:
            return False, "El ID de usuario ya existe."
        
        self.__ids_usuarios.add(usuario.id_usuario)
        self.__usuarios[usuario.id_usuario] = usuario
        return True, f"Usuario '{usuario.nombre}' registrado exitosamente."

    def dar_baja_usuario(self, id_usuario):
        if id_usuario not in self.__ids_usuarios:
            return False, "Usuario no encontrado."
        
        usuario = self.__usuarios[id_usuario]
        if len(usuario.libros_prestados) > 0:
            return False, "El usuario tiene libros pendientes por devolver."
        
        # Elimina del conjunto y del diccionario
        self.__ids_usuarios.remove(id_usuario)
        del self.__usuarios[id_usuario]
        return True, "Usuario dado de baja exitosamente."

    # PRÉSTAMOS Y DEVOLUCIONES
    def prestar_libro(self, isbn, id_usuario):
        if id_usuario not in self.__ids_usuarios:
            return False, "Usuario no registrado."
        if isbn not in self.__libros_disponibles:
            return False, "Libro no disponible o no existe."

        # Saca el libro del diccionario de disponibles
        libro = self.__libros_disponibles.pop(isbn)
        # Lo añade a la lista del usuario
        self.__usuarios[id_usuario].prestar_libro(libro)
        return True, f"Libro prestado exitosamente a {self.__usuarios[id_usuario].nombre}."

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.__ids_usuarios:
            return False, "Usuario no registrado."

        # Retira el libro de la lista del usuario
        libro_devuelto = self.__usuarios[id_usuario].devolver_libro(isbn)
        
        if libro_devuelto:
            # Lo devuelve al diccionario de la biblioteca
            self.__libros_disponibles[isbn] = libro_devuelto
            return True, f"Libro devuelto exitosamente por {self.__usuarios[id_usuario].nombre}."
        
        return False, "El usuario no tiene asignado este libro."

    def listar_prestados(self, id_usuario):
        if id_usuario in self.__ids_usuarios:
            return self.__usuarios[id_usuario].libros_prestados
        return None