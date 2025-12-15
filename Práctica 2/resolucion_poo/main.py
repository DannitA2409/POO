from clima_semanal import ClimaSemanal

def ejecutar_programa():
    print("--- SISTEMA DE PROMEDIO CLIMÁTICO (POO Modular) ---")
    
    # Instancia la clase hija 
    clima = ClimaSemanal()

    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    for dia in dias_semana:
        while True: 
            try:
                temp = float(input(f"Ingrese temperatura del {dia}: "))
                clima.agregar_dato(temp) # Método heredado del padre
                break
            except ValueError:
                print("Error: Ingrese un número válido (ej. 24.5).")

    # Cálculo y salida
    promedio = clima.calcular_promedio() # Método polimórfico del hijo
    
    print("-" * 30)
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")
    print("-" * 30)

# Bloque de ejecución principal
if __name__ == "__main__":
    ejecutar_programa()