using DoublyLinkedListApp.Models;
using System;

namespace DoublyLinkedListApp.Controllers
{
    public class ListController
    {
        private DoublyLinkedList list;

        public ListController()
        {
            list = new DoublyLinkedList();
        }

        // Método para agregar un nodo al final de la lista
        public void AddToEnd(int data)
        {
            list.AddToEnd(data);
            Console.WriteLine($"Nodo con valor {data} agregado al final de la lista.");
        }

        // Método para agregar un nodo al inicio de la lista
        public void AddToStart(int data)
        {
            list.AddToStart(data);
            Console.WriteLine($"Nodo con valor {data} agregado al inicio de la lista.");
        }

        // Método para eliminar un nodo por su valor
        public void Remove(int data)
        {
            bool removed = list.Remove(data);
            if (removed)
            {
                Console.WriteLine($"Nodo con valor {data} eliminado de la lista.");
            }
            else
            {
                Console.WriteLine($"Nodo con valor {data} no encontrado en la lista.");
            }
        }

        // Método para imprimir la lista en orden
        public void PrintList()
        {
            Console.WriteLine("Imprimiendo lista en orden:");
            list.PrintList();
        }

        // Método para imprimir la lista en orden inverso
        public void PrintReverse()
        {
            Console.WriteLine("Imprimiendo lista en orden inverso:");
            list.PrintReverse();
        }
    }
}