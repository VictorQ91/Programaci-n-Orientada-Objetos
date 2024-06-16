def calcular_promedio_semanal():
    # Crear una lista para almacenar las temperaturas de la semana
    temperaturas = []

    # Pedir al usuario que ingrese las temperaturas de cada día de la semana
    print("//////////////////////////////////////////////////////")
    print("Ingrese las temperaturas de los 7 días de la semana:")
    print("//////////////////////////////////////////////////////")
    for dia in range(1, 8):
        while True:
            try:
                temp = float(input(f"Día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    # Calcular el promedio
    promedio = sum(temperaturas) / len(temperaturas)

    # Mostrar el resultado
    print("//////////////////////////////////////////////////////")
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")
    print("//////////////////////////////////////////////////////")


# Llamar a la función para ejecutar el programa
calcular_promedio_semanal()