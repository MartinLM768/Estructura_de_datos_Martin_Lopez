namespace DoublyLinkedListApp.Models
{
    public class Node
    {
        public string Data { get; set; }
        public Node Next { get; set; }
        public Node Previous { get; set; }

        public Node(string data)
        {
            Data = data;
            Next = null;
            Previous = null;
        }
    }

    public class DoublyLinkedList
    {
        private Node head;
        private Node tail;

        public void AddToEnd(string data)
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

        public void AddToStart(string data)
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

        public bool Remove(string data)
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

        public string PrintList()
        {
            Node current = head;
            string result = "Lista en orden: ";
            while (current != null)
            {
                result += current.Data + " ";
                current = current.Next;
            }
            return result;
        }

        public string PrintReverse()
        {
            Node current = tail;
            string result = "Lista en orden inverso: ";
            while (current != null)
            {
                result += current.Data + " ";
                current = current.Previous;
            }
            return result;
        }
    }
}