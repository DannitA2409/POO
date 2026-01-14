# servicios/gestion_inventario.py

class GestionInventario:
    def __init__(self):
        # Lista para almacenar las instancias de vehiculos
        self.lista_vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)
        print(f"-> {vehiculo.obtener_detalle()} agregado al inventario.")

    def mostrar_reporte(self):
        print("\n--- REPORTE DE INVENTARIO Y COSTOS ---")
        for v in self.lista_vehiculos:
            # Aquí se demuestra el POLIMORFISMO:
            # Se llama al mismo método 'calcular_impuesto' pero cada objeto
            # responde de forma diferente según su clase (Auto o Moto).
            impuesto = v.calcular_impuesto()
            total = v.get_precio_base() + impuesto
            print(f"{v} | Impuesto: ${impuesto:.2f} | Total: ${total:.2f}")