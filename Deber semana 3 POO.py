class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        print("//////////////////////////////////////////////////////")
        print("Ingrese las temperaturas de los 7 días de la semana:")
        print("//////////////////////////////////////////////////////")
        for dia in range(1, 8):
            while True:
                try:
                    temp = float(input(f"Día {dia}: "))
                    self.temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print("//////////////////////////////////////////////////////")
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")
        print("//////////////////////////////////////////////////////")


clima_semanal = ClimaSemanal()
clima_semanal.ingresar_temperaturas()
clima_semanal.mostrar_promedio()