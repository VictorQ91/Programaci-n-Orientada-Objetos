import os
import subprocess

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def ejecutar_script(ruta_script):
    try:
        print(f"\n--- Ejecutando {os.path.basename(ruta_script)} ---\n")
        subprocess.run(['python', ruta_script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el script: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Deber semana 2.py',
        '2': 'Deber semana 3 POO.py',
        '3': 'Deber semana 3 Programacion Tradicional.py',
        '4': 'Deber semana 5.py',
        '5': 'Deber semana 6 Polimorfismo.py',
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key, script in opciones.items():
            print(f"{key} - {script}")
        print("0 - Salir")

        eleccion = input("Elige una opción para ver el código o presione '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            ejecutar_input = input("\n¿Quieres ejecutar este script? (s/n): ").lower()
            if ejecutar_input == 's':
                ejecutar_script(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()