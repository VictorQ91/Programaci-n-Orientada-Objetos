import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x600")

        # Lista de tareas
        self.task_list = []

        # Campo de entrada para tareas
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Presionar Enter para añadir tarea

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Botones para marcar como completada y eliminar tarea
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            completed_task = f"[Tarea Completada] {task}"
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, completed_task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completar.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
