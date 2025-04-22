using System;

namespace DoublyLinkedListApp.Models
{
    // Clase Nodo que representa un elemento de la lista doblemente enlazada
    public class Node
    {
        public int Data { get; set; }
        public Node Next { get; set; }
        public Node Previous { get; set; }

        public Node(int data)
        {
            Data = data;
            Next = null;
            Previous = null;
        }
    }

    // Clase DoublyLinkedList que implementa la lista doblemente enlazada
    public class DoublyLinkedList
    {
        private Node head;
        private Node tail;

        public DoublyLinkedList()
        {
            head = null;
            tail = null;
        }

        // Método para agregar un nodo al final de la lista
        public void AddToEnd(int data)
        {
            Node newNode = new Node(data);
            if (head == null)
            {
                head = newNode;
                tail = newNode;
            }
            else
            {
                tail.Next = newNode;
                newNode.Previous = tail;
                tail = newNode;
            }
        }

        // Método para agregar un nodo al inicio de la lista
        public void AddToStart(int data)
        {
            Node newNode = new Node(data);
            if (head == null)
            {
                head = newNode;
                tail = newNode;
            }
            else
            {
                newNode.Next = head;
                head.Previous = newNode;
                head = newNode;
            }
        }

        // Método para eliminar un nodo por su valor
        public bool Remove(int data)
        {
            Node current = head;

            while (current != null)
            {
                if (current.Data == data)
                {
                    if (current.Previous != null)
                        current.Previous.Next = current.Next;
                    else
                        head = current.Next;

                    if (current.Next != null)
                        current.Next.Previous = current.Previous;
                    else
                        tail = current.Previous;

                    return true;
                }
                current = current.Next;
            }
            return false;
        }

        // Método para imprimir la lista en orden
        public void PrintList()
        {
            Node current = head;
            Console.WriteLine("Lista en orden:");
            while (current != null)
            {
                Console.Write(current.Data + " ");
                current = current.Next;
            }
            Console.WriteLine();
        }

        // Método para imprimir la lista en orden inverso
        public void PrintReverse()
        {
            Node current = tail;
            Console.WriteLine("Lista en orden inverso:");
            while (current != null)
            {
                Console.Write(current.Data + " ");
                current = current.Previous;
            }
            Console.WriteLine();
        }
    }
}