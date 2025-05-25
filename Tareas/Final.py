import tkinter as tk
from tkinter import simpledialog, messagebox

class Nodo:
    """Clase que representa un nodo del árbol binario."""
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinario:
    """Clase que representa el árbol binario de búsqueda."""
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        """Inserta un dato en el árbol."""
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodo(dato)
            else:
                self._insertar(nodo.izq, dato)
        else:
            if nodo.der is None:
                nodo.der = Nodo(dato)
            else:
                self._insertar(nodo.der, dato)

    def inorden(self):
        """Recorrido In orden: Izquierda, Raíz, Derecha.
        Devuelve los elementos en orden ascendente en un ABB.
        """
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is None:
            return []
        return self._inorden(nodo.izq) + [nodo.dato] + self._inorden(nodo.der)

    def preorden(self):
        """Recorrido Pre orden: Raíz, Izquierda, Derecha.
        Útil para copiar el árbol o evaluar expresiones.
        """
        return self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo is None:
            return []
        return [nodo.dato] + self._preorden(nodo.izq) + self._preorden(nodo.der)

    def postorden(self):
        """Recorrido Post orden: Izquierda, Derecha, Raíz.
        Útil para eliminar el árbol o evaluar expresiones en notación postfija.
        """
        return self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo is None:
            return []
        return self._postorden(nodo.izq) + self._postorden(nodo.der) + [nodo.dato]

class ArbolApp:
    def __init__(self, root):
        self.arbol = ArbolBinario()
        self.root = root
        self.root.title("Árbol Binario de Búsqueda Visual")

        # Botones de menú
        tk.Button(root, text="Insertar dato", width=25, command=self.insertar).pack(pady=2)
        tk.Button(root, text="Imprimir en In orden", width=25, command=self.mostrar_inorden).pack(pady=2)
        tk.Button(root, text="Imprimir en Post orden", width=25, command=self.mostrar_postorden).pack(pady=2)
        tk.Button(root, text="Imprimir en Pre orden", width=25, command=self.mostrar_preorden).pack(pady=2)
        tk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=2)

        self.label_resultado = tk.Label(root, text="", font=("Arial", 12))
        self.label_resultado.pack(pady=10)

        # Diferencia entre In orden y Pre orden:
        # In orden: Recorre primero la izquierda, luego la raíz, luego la derecha.
        # Pre orden: Recorre primero la raíz, luego la izquierda, luego la derecha.
        # En un árbol binario de búsqueda, el recorrido In orden da los datos ordenados.

    def insertar(self):
        valor = simpledialog.askinteger("Insertar dato", "Ingrese el dato (entero):")
        if valor is not None:
            self.arbol.insertar(valor)
            messagebox.showinfo("Insertar", f"Dato {valor} insertado.")

    def mostrar_inorden(self):
        recorrido = self.arbol.inorden()
        self.label_resultado.config(text=f"In orden: {recorrido}")

    def mostrar_postorden(self):
        recorrido = self.arbol.postorden()
        self.label_resultado.config(text=f"Post orden: {recorrido}")

    def mostrar_preorden(self):
        recorrido = self.arbol.preorden()
        self.label_resultado.config(text=f"Pre orden: {recorrido}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArbolApp(root)
    root.mainloop()
    # 8,3,1,6,4,7,10,14,13