from datos_diarios import DatosDiarios

class ClimaSemanal(DatosDiarios): 
    """
    Clase Hija.
    Hereda de DatosDiarios y especializa el cálculo para el clima.
    """

    # Sobrescribe el método del padre
    def calcular_promedio(self):
        # Usa el método protegido del padre para obtener la lista
        datos = self._obtener_datos()
        
        if not datos:
            return 0.0
        
        suma = sum(datos)
        cantidad = len(datos)
        return suma / cantidad