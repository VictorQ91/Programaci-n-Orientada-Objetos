import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("ADVERTENCIA", "El campo de texto está vacío.")

# Función para limpiar datos
def limpiar_datos():
    entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
    lista_datos.delete(0, tk.END)  # Limpiar la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("APLICACIÓN GUI BASICA")

# Crear y ubicar los componentes en la ventana
etiqueta_instrucciones = tk.Label(ventana, text="Ingrese un dato y presione 'Agregar' para añadirlo a la lista.")
etiqueta_instrucciones.pack(pady=10)

entrada_texto = tk.Entry(ventana, width=50)
entrada_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()