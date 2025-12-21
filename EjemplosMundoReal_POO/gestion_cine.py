from pelicula import PeliculaRegular, Pelicula3D
from sala import Sala

class Cine:
    def __init__(self):
        self.cartelera = []
        self.salas = [Sala(1, 50), Sala(2, 20)] # Salas predefinidas

    def agregar_pelicula(self, peli):
        self.cartelera.append(peli)

    def mostrar_cartelera(self):
        print("\n--- CARTELERA DISPONIBLE ---")
        for i, peli in enumerate(self.cartelera):
            # Polimorfismo: cada peli sabe su precio según su tipo
            print(f"{i+1}. {peli.obtener_titulo()} - Precio: ${peli.calcular_precio():.2f}")

    def realizar_venta(self, indice_peli, cant_personas):
        if 0 <= indice_peli < len(self.cartelera):
            peli = self.cartelera[indice_peli]
            # Usar la Sala 1 por defecto
            if self.salas[0].ocupar_asientos(cant_personas):
                total = peli.calcular_precio() * cant_personas
                print(f"\nVENTA EXITOSA: {peli.obtener_titulo()}")
                print(f"Total a pagar: ${total:.2f}")
            else:
                print("\nERROR: No hay suficiente espacio en la sala.")
        else:
            print("\nERROR: Selección de película no válida.")