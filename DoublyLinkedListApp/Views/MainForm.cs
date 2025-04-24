using DoublyLinkedListApp.Controllers;
using System;
using System.Windows.Forms;

namespace DoublyLinkedListApp.Views
{
    public class MainForm : Form
    {
        private TextBox txtValue;
        private Button btnAddToEnd, btnAddToStart, btnRemove, btnPrintList, btnPrintReverse;
        private ListController controller;
        private TextBox txtOutput;

        public MainForm()
        {
            controller = new ListController();
            InitializeComponents();
        }

        private void InitializeComponents()
        {
            this.Text = "Lista Doble Enlazada";
            this.Size = new System.Drawing.Size(400, 300);

            txtValue = new TextBox { Location = new System.Drawing.Point(20, 20), Width = 200 };
            btnAddToEnd = new Button { Text = "Agregar al Final", Location = new System.Drawing.Point(20, 60) };
            btnAddToStart = new Button { Text = "Agregar al Inicio", Location = new System.Drawing.Point(20, 100) };
            btnRemove = new Button { Text = "Eliminar Nodo", Location = new System.Drawing.Point(20, 140) };
            btnPrintList = new Button { Text = "Imprimir Lista", Location = new System.Drawing.Point(20, 180) };
            btnPrintReverse = new Button { Text = "Imprimir Inverso", Location = new System.Drawing.Point(20, 220) };
            txtOutput = new TextBox { Location = new System.Drawing.Point(150, 60), Width = 200, Height = 180, Multiline = true, ReadOnly = true };

            btnAddToEnd.Click += (s, e) =>
            {
                if (int.TryParse(txtValue.Text, out int value))
                {
                    controller.AddToEnd(value);
                    txtOutput.Text = "Nodo agregado al final.";
                }
            };

            btnAddToStart.Click += (s, e) =>
            {
                if (int.TryParse(txtValue.Text, out int value))
                {
                    controller.AddToStart(value);
                    txtOutput.Text = "Nodo agregado al inicio.";
                }
            };

            btnRemove.Click += (s, e) =>
            {
                if (int.TryParse(txtValue.Text, out int value))
                {
                    if (controller.Remove(value))
                        txtOutput.Text = "Nodo eliminado.";
                    else
                        txtOutput.Text = "Nodo no encontrado.";
                }
            };

            btnPrintList.Click += (s, e) => txtOutput.Text = controller.PrintList();
            btnPrintReverse.Click += (s, e) => txtOutput.Text = controller.PrintReverse();

            this.Controls.Add(txtValue);
            this.Controls.Add(btnAddToEnd);
            this.Controls.Add(btnAddToStart);
            this.Controls.Add(btnRemove);
            this.Controls.Add(btnPrintList);
            this.Controls.Add(btnPrintReverse);
            this.Controls.Add(txtOutput);
        }
    }
}