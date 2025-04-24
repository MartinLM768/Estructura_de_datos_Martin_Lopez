using DoublyLinkedListApp.Models;

namespace DoublyLinkedListApp.Controllers
{
    public class ListController
    {
        private DoublyLinkedList list;

        public ListController()
        {
            list = new DoublyLinkedList();
        }

        public void AddToEnd(int data) => list.AddToEnd(data);
        public void AddToStart(int data) => list.AddToStart(data);
        public bool Remove(int data) => list.Remove(data);
        public string PrintList() => list.PrintList();
        public string PrintReverse() => list.PrintReverse();
    }
}