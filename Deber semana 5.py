# Este programa calcula el área de un círculo basado en el radio proporcionado por el usuario.
# Utiliza diferentes tipos de datos: integer, float, string, boolean.

import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    # El área de un círculo se calcula usando la fórmula: área = π * radio^2
    area = math.pi * radio ** 2
    return area

def es_numero_positivo(numero):
    """Verifica si un número es positivo."""
    # Verifica que el número sea mayor que cero
    return numero > 0

# Solicitar al usuario que ingrese el radio del círculo
radio_usuario = input("Introduce el radio del círculo: ")

# Intentar convertir la entrada del usuario a un float
try:
    radio = float(radio_usuario)
except ValueError:
    print("Error: El valor ingresado no es un número válido.")
    radio = 0.0

# Verificar que el radio sea un número positivo
if es_numero_positivo(radio):
    # Calcular el área del círculo
    area_circulo = calcular_area_circulo(radio)
    # Imprimir el resultado
    print(f"El área del círculo con radio {radio} es {area_circulo:.2f}")
else:
    print("Error: El radio debe ser un número positivo.")