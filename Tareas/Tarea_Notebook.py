class Nodo:
    """
    Clase Nodo que representa un cliente en la lista circular.
    """
    def __init__(self, cedula, nombre):
        self.cedula = cedula  # Cédula del cliente
        self.nombre = nombre  # Nombre del cliente
        self.siguiente = None  # Puntero al siguiente nodo


class ListaCircular:
    """
    Clase ListaCircular que implementa una lista circular dinámica.
    """
    def __init__(self):
        self.inicio = None  # Nodo inicial de la lista

    def insertar_cliente(self, cedula, nombre):
        """
        Inserta un nuevo cliente en la lista circular.
        """
        nuevo = Nodo(cedula, nombre)  # Crear un nuevo nodo
        if self.inicio is None:
            # Si la lista está vacía, el nuevo nodo apunta a sí mismo
            self.inicio = nuevo
            nuevo.siguiente = nuevo
        else:
            # Si la lista no está vacía, insertar al final
            actual = self.inicio
            while actual.siguiente != self.inicio:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.inicio

    def listar_clientes(self):
        """
        Lista todos los clientes desde el primer nodo hasta el último.
        """
        if self.inicio is None:
            print("La lista está vacía.")
            return

        actual = self.inicio
        print("Clientes en la lista circular:")
        while True:
            print(f"Cédula: {actual.cedula}, Nombre: {actual.nombre}")
            actual = actual.siguiente
            if actual == self.inicio:
                break


def menu():
    """
    Función principal que muestra el menú de opciones y gestiona la interacción con el usuario.
    """
    lista = ListaCircular()

    while True:
        print("\nMenú de Opciones:")
        print("1. Insertar Cliente")
        print("2. Listar Clientes hacia la derecha")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("Ingrese la cédula del cliente: ")
            nombre = input("Ingrese el nombre del cliente: ")
            lista.insertar_cliente(cedula, nombre)
            print("Cliente insertado correctamente.")
        elif opcion == "2":
            lista.listar_clientes()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    menu()