import os
import subprocess

EXCLUIR_CARPETAS = {'.git', '__pycache__'}

def listar_carpetas(ruta):
    carpetas = []
    for item in os.scandir(ruta):
        if item.is_dir():
            if item.name in EXCLUIR_CARPETAS:
                continue
            if item.name.startswith('.'):
                continue
            carpetas.append(item.name)
    return sorted(carpetas)

def listar_scripts(ruta):
    scripts = []
    for item in os.scandir(ruta):
        if item.is_file() and item.name.endswith('.py'):
            scripts.append(item.name)
    return sorted(scripts)

def mostrar_codigo(ruta_script):            
    # Asegura que la ruta al script sea absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        try:
            with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
                codigo = archivo.read()
        except UnicodeDecodeError:
            # Fallback para archivos con otra codificacion (ej. ANSI/Windows-1252)
            with open(ruta_script_absoluta, 'r', encoding='cp1252') as archivo:
                codigo = archivo.read()
        print(f"\n--- Codigo de {ruta_script} ---\n")
        print(codigo)
        return codigo
    except FileNotFoundError:
        print("El archivo no se encontro.")
        return None
    except Exception as e:
        print(f"Ocurrio un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrio un error al ejecutar el codigo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el Dashboard.py
    ruta_base = os.path.dirname(__file__)

    while True:
        carpetas_principales = listar_carpetas(ruta_base)

        print("\nMenu Principal - Dashboard")
        if not carpetas_principales:
            print("No se encontraron carpetas en el repositorio.")
            print("Saliendo del programa.")
            break

        for i, carpeta in enumerate(carpetas_principales, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Salir")

        eleccion = input("Elige una carpeta o '0' para salir: ")
        if eleccion == '0':
            print("Saliendo del programa.")
            break
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(carpetas_principales):
                    volver_menu = mostrar_sub_menu(os.path.join(ruta_base, carpetas_principales[indice]))
                    if volver_menu:
                        continue
                else:
                    print("Opcion no valida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opcion no valida. Por favor, intenta de nuevo.")

def mostrar_sub_menu(ruta_carpeta):
    while True:
        sub_carpetas = listar_carpetas(ruta_carpeta)
        scripts = listar_scripts(ruta_carpeta)

        if not sub_carpetas and not scripts:
            print("\nNo se encontraron subcarpetas ni scripts en esta ruta.")
            input("Presiona Enter para regresar.")
            return False

        print("\nSubmenu - Selecciona una carpeta o scripts")
        entradas = []

        if scripts:
            entradas.append(("scripts", ruta_carpeta, "Ver scripts de esta carpeta"))

        for carpeta in sub_carpetas:
            entradas.append(("carpeta", os.path.join(ruta_carpeta, carpeta), carpeta))

        for i, entrada in enumerate(entradas, start=1):
            print(f"{i} - {entrada[2]}")
        print("0 - Regresar")

        eleccion = input("Elige una opcion o '0' para regresar: ")
        if eleccion == '0':
            return False
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(entradas):
                    tipo, ruta, _ = entradas[indice]
                    if tipo == "scripts":
                        volver_menu = mostrar_scripts(ruta)
                        if volver_menu:
                            return True
                    else:
                        volver_menu = mostrar_sub_menu(ruta)
                        if volver_menu:
                            return True
                else:
                    print("Opcion no valida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opcion no valida. Por favor, intenta de nuevo.")

def mostrar_scripts(ruta_sub_carpeta):
    scripts = listar_scripts(ruta_sub_carpeta)

    if not scripts:
        print("\nNo se encontraron scripts en esta carpeta.")
        input("Presiona Enter para regresar.")
        return False

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenu anterior")
        print("9 - Regresar al menu principal")

        eleccion = input("Elige un script, '0' para regresar o '9' para ir al menu principal: ")
        if eleccion == '0':
            return False
        elif eleccion == '9':
            return True
        else:
            try:
                indice = int(eleccion) - 1
                if 0 <= indice < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("Desea ejecutar el script? (1: Si, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecuto el script.")
                        else:
                            print("Opcion no valida. Regresando al menu de scripts.")
                        input("\nPresiona Enter para volver al menu de scripts.")
                else:
                    print("Opcion no valida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opcion no valida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
