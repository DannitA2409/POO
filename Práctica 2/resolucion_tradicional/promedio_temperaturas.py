# RESOLUCION CON PROGRAMACIÓN TRADICIONAL

def ingresar_temperaturas_diarias():
    """
    Pide al usuario las temperaturas de 7 días y las devuelve en una lista.
    """
    temperaturas = []
    print("--- Ingreso de Temperaturas Semanales ---")
    for i in range(7):
        temp = float(input(f"Ingrese temperatura día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio_semanal(lista_temperaturas):
    """
    Recibe una lista de temperaturas y retorna el promedio.
    """
    suma = sum(lista_temperaturas)
    cantidad = len(lista_temperaturas)
    promedio = suma / cantidad
    return promedio

# Bloque Principal
if __name__ == "__main__":
    # Llama a la función de entrada
    datos = ingresar_temperaturas_diarias()
    
    # Llama a la función de cálculo
    resultado = calcular_promedio_semanal(datos)
    
    # Muestra resultado
    print(f"El promedio semanal es: {resultado:.2f}")