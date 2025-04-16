import java.util.Scanner;

// Clase Nodo que representa cada cliente en la lista doble
class Nodo {
    int cedula;
    String nombre;
    Nodo siguiente;
    Nodo anterior;

    public Nodo(int cedula, String nombre) {
        this.cedula = cedula;
        this.nombre = nombre;
        this.siguiente = null;
        this.anterior = null;
    }
}

// Clase ListaDoble que implementa las operaciones sobre la lista doblemente enlazada
class ListaDoble {
    private Nodo cabeza;

    public ListaDoble() {
        this.cabeza = null;
    }

    // Método para insertar un cliente de forma ordenada
    public void insertarCliente(int cedula, String nombre) {
        Nodo nuevo = new Nodo(cedula, nombre);
        if (cabeza == null) {
            cabeza = nuevo;
        } else {
            Nodo actual = cabeza;
            Nodo anterior = null;

            // Buscar la posición correcta para insertar
            while (actual != null && actual.cedula < cedula) {
                anterior = actual;
                actual = actual.siguiente;
            }

            if (anterior == null) { // Insertar al inicio
                nuevo.siguiente = cabeza;
                cabeza.anterior = nuevo;
                cabeza = nuevo;
            } else { // Insertar en medio o al final
                nuevo.siguiente = actual;
                nuevo.anterior = anterior;
                anterior.siguiente = nuevo;
                if (actual != null) {
                    actual.anterior = nuevo;
                }
            }
        }
    }

    // Método para listar clientes de izquierda a derecha
    public void listarDerecha() {
        Nodo actual = cabeza;
        System.out.println("Clientes (de izquierda a derecha):");
        while (actual != null) {
            System.out.println("Cédula: " + actual.cedula + ", Nombre: " + actual.nombre);
            actual = actual.siguiente;
        }
    }

    // Método para listar clientes de derecha a izquierda
    public void listarIzquierda() {
        if (cabeza == null) {
            System.out.println("La lista está vacía.");
            return;
        }

        // Ir al último nodo
        Nodo actual = cabeza;
        while (actual.siguiente != null) {
            actual = actual.siguiente;
        }

        System.out.println("Clientes (de derecha a izquierda):");
        while (actual != null) {
            System.out.println("Cédula: " + actual.cedula + ", Nombre: " + actual.nombre);
            actual = actual.anterior;
        }
    }
}

// Clase principal con el menú de opciones
public class Main2 { // Cambiado de Main a Main2
    public static void main(String[] args) {
        ListaDoble lista = new ListaDoble();
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\nMenú de opciones:");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Listar clientes hacia la derecha");
            System.out.println("3. Listar clientes hacia la izquierda");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese la cédula del cliente: ");
                    int cedula = scanner.nextInt();
                    scanner.nextLine(); // Consumir el salto de línea
                    System.out.print("Ingrese el nombre del cliente: ");
                    String nombre = scanner.nextLine();
                    lista.insertarCliente(cedula, nombre);
                    break;
                case 2:
                    lista.listarDerecha();
                    break;
                case 3:
                    lista.listarIzquierda();
                    break;
                case 4:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
        } while (opcion != 4);

        scanner.close();
    }
}