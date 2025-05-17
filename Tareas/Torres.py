import tkinter as tk
from threading import Thread
import time

class HanoiGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Torres de Hanoi Visual")
        self.n = None

        # Interfaz para ingresar la cantidad de discos
        self.frame_input = tk.Frame(master)
        self.label = tk.Label(self.frame_input, text="Ingrese el número de discos:")
        self.label.pack(side=tk.LEFT, padx=5, pady=10)
        self.entry = tk.Entry(self.frame_input, width=5)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.btn_start = tk.Button(self.frame_input, text="Iniciar", command=self.start)
        self.btn_start.pack(side=tk.LEFT, padx=5)
        self.frame_input.pack()

        self.canvas = None
        self.btn_restart = None
        self.btn_prev = None
        self.btn_next = None

        # Para navegación de movimientos
        self.movimientos = []
        self.estados = []
        self.indice = 0

    def start(self):
        try:
            n = int(self.entry.get())
            if n < 1 or n > 8:
                raise ValueError
        except ValueError:
            self.label.config(text="Ingrese un número válido (1-8):", fg="red")
            return

        self.n = n
        self.frame_input.pack_forget()
        if self.canvas:
            self.canvas.destroy()
        if self.btn_restart:
            self.btn_restart.destroy()
        if self.btn_prev:
            self.btn_prev.destroy()
        if self.btn_next:
            self.btn_next.destroy()
        self.canvas = tk.Canvas(self.master, width=600, height=300, bg="white")
        self.canvas.pack()
        self.torres = {'A': list(range(self.n, 0, -1)), 'B': [], 'C': []}
        self.movimientos = []
        self.estados = []
        self.indice = 0
        # Calcular movimientos y estados en un hilo para no congelar la interfaz
        Thread(target=self.precompute).start()

    def precompute(self):
        # Guardar el estado inicial
        self.estados.append(self.copiar_torres())
        self.hanoi(self.n, 'A', 'C', 'B')
        self.indice = 0
        self.draw_torres()
        self.show_navigation_buttons()

    def copiar_torres(self):
        # Devuelve una copia profunda del estado de las torres
        return {k: v.copy() for k, v in self.torres.items()}

    def hanoi(self, n, origen, destino, auxiliar):
        if n == 1:
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.movimientos.append((origen, destino, disco))
            self.estados.append(self.copiar_torres())
        else:
            self.hanoi(n-1, origen, auxiliar, destino)
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
            self.movimientos.append((origen, destino, disco))
            self.estados.append(self.copiar_torres())
            self.hanoi(n-1, auxiliar, destino, origen)

    def draw_torres(self):
        self.canvas.delete("all")
        n = self.n
        estado = self.estados[self.indice]
        # Dibujar las bases de las torres
        for i, torre in enumerate(['A', 'B', 'C']):
            x = 100 + i * 200
            self.canvas.create_rectangle(x-5, 100, x+5, 250, fill="gray")
            self.canvas.create_text(x, 270, text=torre, font=("Arial", 16))
        # Dibujar los discos de abajo hacia arriba, fila por fila
        for fila in range(n):
            y = 240 - (n - 1 - fila) * 20  # Fila 0 es la más baja
            for i, torre in enumerate(['A', 'B', 'C']):
                x = 100 + i * 200
                torre_lista = estado[torre]
                # El disco que va en esta fila (de abajo hacia arriba)
                idx = n - 1 - fila
                if idx < len(torre_lista):
                    disco = torre_lista[idx]
                    ancho = 20 + disco * 30
                    self.canvas.create_rectangle(x - ancho//2, y, x + ancho//2, y + 20, fill="skyblue", outline="black")
                    self.canvas.create_text(x, y + 10, text=str(disco), font=("Arial", 12))
                
        self.master.update()

        # Mensaje de completado
        if self.indice == len(self.estados) - 1:
            self.canvas.create_text(300, 20, text="¡Completado!", font=("Arial", 18), fill="green")

    def show_navigation_buttons(self):
        # Botón anterior
        self.btn_prev = tk.Button(self.master, text="Anterior", command=self.prev_step)
        self.btn_prev.pack(side=tk.LEFT, padx=10, pady=10)
        # Botón siguiente
        self.btn_next = tk.Button(self.master, text="Siguiente", command=self.next_step)
        self.btn_next.pack(side=tk.LEFT, padx=10, pady=10)
        # Botón reiniciar
        self.btn_restart = tk.Button(self.master, text="Reiniciar", command=self.reset)
        self.btn_restart.pack(side=tk.LEFT, padx=10, pady=10)
        self.update_buttons()

    def update_buttons(self):
        # Deshabilitar botones si estamos al inicio o al final
        if self.indice <= 0:
            self.btn_prev.config(state=tk.DISABLED)
        else:
            self.btn_prev.config(state=tk.NORMAL)
        if self.indice >= len(self.estados) - 1:
            self.btn_next.config(state=tk.DISABLED)
        else:
            self.btn_next.config(state=tk.NORMAL)

    def prev_step(self):
        if self.indice > 0:
            self.indice -= 1
            self.draw_torres()
            self.update_buttons()

    def next_step(self):
        if self.indice < len(self.estados) - 1:
            self.indice += 1
            self.draw_torres()
            self.update_buttons()

    def reset(self):
        # Limpiar canvas y botones
        if self.canvas:
            self.canvas.destroy()
        if self.btn_restart:
            self.btn_restart.destroy()
        if self.btn_prev:
            self.btn_prev.destroy()
        if self.btn_next:
            self.btn_next.destroy()
        # Limpiar entrada y mensaje
        self.entry.delete(0, tk.END)
        self.label.config(text="Ingrese el número de discos:", fg="black")
        self.frame_input.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiGUI(root)
    root.mainloop()