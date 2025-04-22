using DoublyLinkedListApp.Controllers;
using System;
using System.Windows.Forms;

namespace DoublyLinkedListApp.Views
{
    public partial class MainForm : Form
    {
        private ListController controller;

        public MainForm()
        {
            InitializeComponent();
            controller = new ListController();
        }

        private void btnAddToEnd_Click(object sender, EventArgs e)
        {
            if (int.TryParse(txtValue.Text, out int value))
            {
                controller.AddToEnd(value);
                MessageBox.Show($"Nodo con valor {value} agregado al final de la lista.");
                txtValue.Clear();
            }
            else
            {
                MessageBox.Show("Por favor, ingrese un valor válido.");
            }
        }

        private void btnAddToStart_Click(object sender, EventArgs e)
        {
            if (int.TryParse(txtValue.Text, out int value))
            {
                controller.AddToStart(value);
                MessageBox.Show($"Nodo con valor {value} agregado al inicio de la lista.");
                txtValue.Clear();
            }
            else
            {
                MessageBox.Show("Por favor, ingrese un valor válido.");
            }
        }

        private void btnRemove_Click(object sender, EventArgs e)
        {
            if (int.TryParse(txtValue.Text, out int value))
            {
                controller.Remove(value);
                txtValue.Clear();
            }
            else
            {
                MessageBox.Show("Por favor, ingrese un valor válido.");
            }
        }

        private void btnPrintList_Click(object sender, EventArgs e)
        {
            controller.PrintList();
        }

        private void btnPrintReverse_Click(object sender, EventArgs e)
        {
            controller.PrintReverse();
        }
    }
}