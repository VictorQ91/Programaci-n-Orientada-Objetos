# Definición de la clase 'Animal'
class Animal:
    def __init__(self, nombre):
        self.__nombre = nombre  # Atributo privado usando '__'

    def get_nombre(self):
        return self.__nombre

    def comer(self):
        return "El animal está comiendo."


# Definición de la clase derivada 'Perro', hereda de 'Animal'
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza  # Atributo privado usando '__'

    def get_raza(self):
        return self.__raza

    # Método sobreescrito para mostrar comportamiento específico del perro
    def comer(self):
        return f"{self.get_nombre()} está comiendo croquetas."


# Función principal
def main():
    # Crear una instancia de la clase 'Perro'
    mi_perro = Perro("Firulais", "Labrador")

    # Acceder a métodos de la clase
    print(f"Nombre del perro: {mi_perro.get_nombre()}")
    print(f"Raza del perro: {mi_perro.get_raza()}")

    # Demostrar polimorfismo: llamar al método 'comer' de ambas clases
    print(mi_perro.comer())  # Polimorfismo: llama al método sobreescrito de la clase derivada

if __name__ == "__main__":
    main()
