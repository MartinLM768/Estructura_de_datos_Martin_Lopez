import java.util.Scanner;

public class Main {

    // Clase Cliente dentro de Main
    static class Cliente {
        int cedula;
        String nombre;
        Cliente siguiente;

        public Cliente(int cedula, String nombre) {
            this.cedula = cedula;
            this.nombre = nombre;
            this.siguiente = null;
        }
    }

    // Clase ListaSimple dentro de Main
    static class ListaSimple {
        private Cliente cabeza;

        public void insertarCliente(int cedula, String nombre) {
            Cliente nuevo = new Cliente(cedula, nombre);

            if (cabeza == null || cabeza.cedula > cedula) {
                nuevo.siguiente = cabeza;
                cabeza = nuevo;
            } else {
                Cliente actual = cabeza;
                while (actual.siguiente != null && actual.siguiente.cedula < cedula) {
                    actual = actual.siguiente;
                }
                nuevo.siguiente = actual.siguiente;
                actual.siguiente = nuevo;
            }
            System.out.println("Cliente insertado correctamente.");
        }

        public void listarClientes() {
            if (cabeza == null) {
                System.out.println("La lista está vacía.");
                return;
            }
            Cliente actual = cabeza;
            System.out.println("Lista de clientes:");
            while (actual != null) {
                System.out.println("Cédula: " + actual.cedula + ", Nombre: " + actual.nombre);
                actual = actual.siguiente;
            }
        }
    }

    public static void main(String[] args) {
        ListaSimple lista = new ListaSimple();
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\nMenú de Opciones:");
            System.out.println("1. Insertar Cliente");
            System.out.println("2. Listar Clientes");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese la cédula del cliente: ");
                    int cedula = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Ingrese el nombre del cliente: ");
                    String nombre = scanner.nextLine();
                    lista.insertarCliente(cedula, nombre);
                    break;

                case 2:
                    lista.listarClientes();
                    break;

                case 3:
                    System.out.println("Saliendo de la aplicación...");
                    break;

                default:
                    System.out.println("Opción inválida. Por favor, intente nuevamente.");
            }
        } while (opcion != 3);

        scanner.close();
    }
}
