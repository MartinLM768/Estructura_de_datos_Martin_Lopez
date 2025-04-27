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

        public void AddToEnd(string data) => list.AddToEnd(data);
        public void AddToStart(string data) => list.AddToStart(data);
        public bool Remove(string data) => list.Remove(data);
        public string PrintList() => list.PrintList();
        public string PrintReverse() => list.PrintReverse();
    }
}