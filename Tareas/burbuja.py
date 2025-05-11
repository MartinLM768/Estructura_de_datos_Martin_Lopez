def metodo_burbuja(lista):
    """
    Método de ordenamiento Burbuja.
    Recorre repetidamente la lista, comparando elementos adyacentes y
    los intercambia si están en el orden incorrecto.
    """
    n = len(lista)
    for i in range(n):
        print(f"Iteración {i + 1}: {lista}")  # Mostrar el estado de la lista en cada iteración
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print(f"Lista ordenada: {lista}")
    return lista


def metodo_secuencial(lista):
    """
    Método de ordenamiento Secuencial (Selección).
    Encuentra el elemento más pequeño y lo coloca en la posición correcta.
    """
    n = len(lista)
    for i in range(n):
        # Encontrar el índice del elemento más pequeño
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambiar el elemento más pequeño con el primer elemento no ordenado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
        print(f"Paso {i + 1}: {lista}")  # Mostrar el estado de la lista en cada paso
    print(f"Lista ordenada: {lista}")
    return lista


def metodo_quicksort(lista, profundidad=0):
    """
    Método de ordenamiento Quicksort.
    Divide y conquista: selecciona un pivote, divide la lista en dos sublistas
    y las ordena recursivamente.
    """
    if len(lista) <= 1:
        return lista  # Caso base: una lista vacía o con un solo elemento ya está ordenada
    else:
        pivote = lista[0]  # Selecciona el primer elemento como pivote
        menores = [x for x in lista[1:] if x <= pivote]  # Elementos menores o iguales al pivote
        mayores = [x for x in lista[1:] if x > pivote]  # Elementos mayores al pivote
        print(f"{'  ' * profundidad}Pivote: {pivote}, Menores: {menores}, Mayores: {mayores}")
        # Llamadas recursivas para ordenar las sublistas y concatenar el resultado
        return metodo_quicksort(menores, profundidad + 1) + [pivote] + metodo_quicksort(mayores, profundidad + 1)
def menu():
    """
    Función principal que muestra el menú de opciones y gestiona la interacción con el usuario.
    """
    while True:
        print("\nMenú de Métodos de Ordenamiento:")
        print("1. Método Burbuja")
        print("2. Método Secuencial")
        print("3. Método Quicksort")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion in ["1", "2", "3"]:
            # Pedir al usuario que ingrese una lista de números
            entrada = input("Ingrese una lista de números separados por comas: ")
            lista = [int(x) for x in entrada.split(",")]

            if opcion == "1":
                print("Ordenando con Método Burbuja:")
                metodo_burbuja(lista)
            elif opcion == "2":
                print("Ordenando con Método Secuencial:")
                metodo_secuencial(lista)
            elif opcion == "3":
                print("Ordenando con Método Quicksort:")
                lista_ordenada = metodo_quicksort(lista)
                print(f"Lista ordenada: {lista_ordenada}")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")
# Ejecutar el programa
if __name__ == "__main__":
    menu()    