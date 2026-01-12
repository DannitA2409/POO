from circulo import Circulo
from rectangulo import Rectangulo

def mostrar_menu():
    print("\n================================")
    print("   SISTEMA DE CÁLCULO DE ÁREAS")
    print("================================")
    print("1. Calcular área de un Círculo")
    print("2. Calcular área de un Rectángulo")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    return opcion




def ejecutar_programa():
    continuar = True # Variable Boolean para el ciclo

    while continuar:
        opcion = mostrar_menu()

        if opcion == "1":
            # Manejo de datos tipo Float e Integer
            try:
                r = float(input("Ingrese el radio del círculo: "))
                mi_circulo = Circulo(r)
                mi_circulo.calcular_area()
                mi_circulo.mostrar_info()
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

        elif opcion == "2":
            try:
                b = float(input("Ingrese la base: "))
                a = float(input("Ingrese la altura: "))
                mi_rectangulo = Rectangulo(b, a)
                mi_rectangulo.calcular_area()
                mi_rectangulo.mostrar_info()
            except ValueError:
                print("Error: Ingrese valores numéricos.")

        elif opcion == "3":
            print("Gracias por usar el programa. ¡Adiós!")
            continuar = False # Cambia el estado para salir del ciclo
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()