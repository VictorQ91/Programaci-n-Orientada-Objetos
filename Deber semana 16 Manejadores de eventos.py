import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas POO")
        self.root.geometry("600x600")

        # Lista de tareas
        self.tasks = []

        # Crear widgets
        self.create_widgets()

        # Asociar atajos de teclado
        self.root.bind('<Return>', self.add_task)  # Tecla Enter para añadir tarea
        self.root.bind('<c>', self.complete_task)  # Tecla C para completar tarea
        self.root.bind('<Delete>', self.delete_task)  # Tecla Delete para eliminar tarea
        self.root.bind('<Escape>', lambda e: self.root.quit())  # Tecla Escape para cerrar

    def create_widgets(self):
        # Campo de entrada para nueva tarea
        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Botón para completar tarea
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía")

    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(tk.END, f"{task} (Completada)")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completar")

    def delete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
