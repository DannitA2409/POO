from libro import Libro
from revista import Revista
from usuario import Usuario
from prestamo import Prestamo

materiales = []
usuarios = []

def registrar_libro():
    titulo = input("Título: ")
    codigo = input("Código: ")
    autor = input("Autor: ")
    materiales.append(Libro(titulo, codigo, autor))

def registrar_revista():
    titulo = input("Título: ")
    codigo = input("Código: ")
    numero = input("Número: ")
    materiales.append(Revista(titulo, codigo, numero))

def registrar_usuario():
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    usuarios.append(Usuario(nombre, cedula))

def listar_materiales():
    if not materiales:
        print("No hay materiales")
        return
    for m in materiales:
        print(m.mostrar_info())

def buscar_material(codigo):
    for m in materiales:
        if m._codigo == codigo:
            return m
    return None

def buscar_usuario(cedula):
    for u in usuarios:
        if u._cedula == cedula:
            return u
    return None

def prestar_material():
    cedula = input("Cédula del usuario: ")
    usuario = buscar_usuario(cedula)
    if not usuario:
        print("Usuario no encontrado")
        return

    codigo = input("Código del material: ")
    material = buscar_material(codigo)
    if not material:
        print("Material no encontrado")
        return

    prestamo = Prestamo(usuario, material)
    if prestamo.realizar_prestamo():
        print("Préstamo realizado")
    else:
        print("El material no está disponible")

def devolver_material():
    codigo = input("Código del material: ")
    material = buscar_material(codigo)
    if material and not material.esta_disponible():
        material.devolver()
        print("Material devuelto")
    else:
        print("Material no encontrado o ya disponible")

while True:
    print("\n--- BIBLIOTECA ---")
    print("1. Registrar libro")
    print("2. Registrar revista")
    print("3. Registrar usuario")
    print("4. Listar materiales")
    print("5. Prestar material")
    print("6. Devolver material")
    print("7. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar_libro()
    elif opcion == "2":
        registrar_revista()
    elif opcion == "3":
        registrar_usuario()
    elif opcion == "4":
        listar_materiales()
    elif opcion == "5":
        prestar_material()
    elif opcion == "6":
        devolver_material()
    elif opcion == "7":
        break
    else:
        print("Opción inválida")
