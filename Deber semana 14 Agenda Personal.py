import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AGENDA PERSONAL 2024")
        self.root.geometry("600x500")

        # Estilo para los botones
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 10))
        self.style.configure("Add.TButton", background="green", foreground="black")
        self.style.map("Add.TButton", background=[("active", "yellow")])

        self.style.configure("Delete.TButton", background="red", foreground="black")
        self.style.map("Delete.TButton", background=[("active", "yellow")])

        self.style.configure("Exit.TButton", background="blue", foreground="black")
        self.style.map("Exit.TButton", background=[("active", "yellow")])

        # Frame para la lista de eventos (TreeView)
        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(pady=20)

        self.tree = ttk.Treeview(self.tree_frame, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para los campos de entrada y botones
        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        ttk.Label(self.entry_frame, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(self.entry_frame, date_pattern="y-mm-dd")
        self.date_entry.grid(row=0, column=1)

        ttk.Label(self.entry_frame, text="Hora:").grid(row=1, column=0)
        self.time_entry = ttk.Entry(self.entry_frame)
        self.time_entry.grid(row=1, column=1)

        ttk.Label(self.entry_frame, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = ttk.Entry(self.entry_frame)
        self.desc_entry.grid(row=2, column=1)

        # Frame para los botones
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = ttk.Button(self.button_frame, text="Agregar Evento", style="Add.TButton", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = ttk.Button(self.button_frame, text="Eliminar Evento Seleccionado", style="Delete.TButton", command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.exit_button = ttk.Button(self.button_frame, text="Salir", style="Exit.TButton", command=self.root.quit)
        self.exit_button.grid(row=0, column=2, padx=5)

    def add_event(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.date_entry.set_date("")
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada inválida", "Todos los campos son obligatorios")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Sin selección", "Selecciona un evento para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()