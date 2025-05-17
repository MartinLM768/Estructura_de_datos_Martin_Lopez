import tkinter as tk
from tkinter import simpledialog, messagebox

class Bicola:
    def __init__(self):
        self.lista = []

    def insertar_derecha(self, valor):
        self.lista.append(valor)

    def insertar_izquierda(self, valor):
        self.lista.insert(0, valor)

    def atender_derecha(self):
        if self.lista:
            return self.lista.pop()
        else:
            return None

    def atender_izquierda(self):
        if self.lista:
            return self.lista.pop(0)
        else:
            return None

    def listar(self):
        return self.lista.copy()

class BicolaApp:
    def __init__(self, root):
        self.bicola = Bicola()
        self.root = root
        self.root.title("Bicola Visual")

        # Botones de menú
        tk.Button(root, text="Insertar por la derecha", width=25, command=self.insertar_derecha).pack(pady=2)
        tk.Button(root, text="Insertar por la izquierda", width=25, command=self.insertar_izquierda).pack(pady=2)
        tk.Button(root, text="Atender por la derecha", width=25, command=self.atender_derecha).pack(pady=2)
        tk.Button(root, text="Atender por la izquierda", width=25, command=self.atender_izquierda).pack(pady=2)
        tk.Button(root, text="Listar", width=25, command=self.listar).pack(pady=2)
        tk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=2)

    def actualizar_estado(self):
        # No actualices ningún label, deja este método vacío o elimínalo
        pass

    def insertar_derecha(self):
        valor = simpledialog.askstring("Insertar por la derecha", "Ingrese el valor:")
        if valor is not None:
            self.bicola.insertar_derecha(valor)
            self.actualizar_estado()

    def insertar_izquierda(self):
        valor = simpledialog.askstring("Insertar por la izquierda", "Ingrese el valor:")
        if valor is not None:
            self.bicola.insertar_izquierda(valor)
            self.actualizar_estado()

    def atender_derecha(self):
        valor = self.bicola.atender_derecha()
        if valor is not None:
            messagebox.showinfo("Atender por la derecha", f"Atendido: {valor}")
        else:
            messagebox.showwarning("Atender por la derecha", "La bicola está vacía.")
        self.actualizar_estado()

    def atender_izquierda(self):
        valor = self.bicola.atender_izquierda()
        if valor is not None:
            messagebox.showinfo("Atender por la izquierda", f"Atendido: {valor}")
        else:
            messagebox.showwarning("Atender por la izquierda", "La bicola está vacía.")
        self.actualizar_estado()

    def listar(self):
        messagebox.showinfo("Listar", f"Bicola: {self.bicola.listar()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BicolaApp(root)
    root.mainloop()