# Ejemplo del Mundo Real

## Sistema de Gestión de Cine (POO)
Este proyecto es un sistema de reservas de cine desarrollado en Python para practicar los pilares fundamentales de la Programación Orientada a Objetos (POO). El sistema permite gestionar películas, salas y ventas de entradas a través de una interfaz de consola.

### Características
Gestión de Cartelera: Diferenciación entre películas regulares y 3D.
Control de Salas: Manejo de capacidad y disponibilidad de asientos.
Venta de Entradas: Interfaz interactiva para el usuario.
Arquitectura Modular: El código está dividido en varios scripts que interactúan entre sí.

### Estructura del Proyecto
El código se divide en los siguientes módulos:
pelicula.py: Contiene la clase base Pelicula y sus subclases (Herencia).
sala.py: Gestiona la lógica de los espacios físicos y capacidad (Encapsulamiento).
gestion_cine.py: Actúa como controlador para coordinar las ventas y la cartelera.
main.py: Punto de entrada del programa con el menú interactivo.

### Conceptos de POO Aplicados
Herencia: Se utiliza una clase base Pelicula de la cual heredan PeliculaRegular y Pelicula3D.
Encapsulamiento: Uso de atributos protegidos (_) y privados (__) para proteger la integridad de los datos (como el conteo de asientos).
Polimorfismo: El método calcular_precio() se comporta de forma distinta dependiendo del tipo de objeto (Regular o 3D) sin necesidad de condicionales complejos.