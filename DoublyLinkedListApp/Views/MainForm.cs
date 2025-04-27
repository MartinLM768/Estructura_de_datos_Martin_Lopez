using DoublyLinkedListApp.Controllers;
using System;
using System.Windows.Forms;

namespace DoublyLinkedListApp.Views
{
    public class MainForm : Form
    {
        private TextBox txtValue;
        private Button btnAddToEnd, btnAddToStart, btnRemove, btnPrintList, btnPrintReverse;
        private Label lblInstructions, lblOutput;
        private TextBox txtOutput;
        private ListController controller;

        public MainForm()
        {
            controller = new ListController();
            InitializeComponents();
        }

        private void InitializeComponents()
        {
            // Configuración del formulario
            this.Text = "Lista Doble Enlazada (Strings)";
            this.Size = new System.Drawing.Size(500, 400);
            this.StartPosition = FormStartPosition.CenterScreen;

            // Etiqueta de instrucciones
            lblInstructions = new Label
            {
                Text = "Ingrese un valor para la lista:",
                Location = new System.Drawing.Point(20, 20),
                AutoSize = true
            };

            // Cuadro de texto para ingresar valores
            txtValue = new TextBox
            {
                Location = new System.Drawing.Point(20, 50),
                Width = 200
            };

            // Botón para agregar al final
            btnAddToEnd = new Button
            {
                Text = "Agregar al Final",
                Location = new System.Drawing.Point(20, 90),
                Width = 150,
                Height = 40
            };
            btnAddToEnd.Click += (s, e) =>
            {
                string value = txtValue.Text;
                if (!string.IsNullOrWhiteSpace(value))
                {
                    controller.AddToEnd(value);
                    txtOutput.Text = "Nodo agregado al final.";
                    txtValue.Clear();
                }
                else
                {
                    MessageBox.Show("Por favor, ingrese un valor válido.");
                }
            };

            // Botón para agregar al inicio
            btnAddToStart = new Button
            {
                Text = "Agregar al Inicio",
                Location = new System.Drawing.Point(200, 90),
                Width = 150,
                Height = 40
            };
            btnAddToStart.Click += (s, e) =>
            {
                string value = txtValue.Text;
                if (!string.IsNullOrWhiteSpace(value))
                {
                    controller.AddToStart(value);
                    txtOutput.Text = "Nodo agregado al inicio.";
                    txtValue.Clear();
                }
                else
                {
                    MessageBox.Show("Por favor, ingrese un valor válido.");
                }
            };

            // Botón para eliminar un nodo
            btnRemove = new Button
            {
                Text = "Eliminar Nodo",
                Location = new System.Drawing.Point(20, 150),
                Width = 150,
                Height = 40
            };
            btnRemove.Click += (s, e) =>
            {
                string value = txtValue.Text;
                if (!string.IsNullOrWhiteSpace(value))
                {
                    if (controller.Remove(value))
                        txtOutput.Text = "Nodo eliminado.";
                    else
                        txtOutput.Text = "Nodo no encontrado.";
                    txtValue.Clear();
                }
                else
                {
                    MessageBox.Show("Por favor, ingrese un valor válido.");
                }
            };

            // Botón para imprimir la lista en orden
            btnPrintList = new Button
            {
                Text = "Imprimir Lista",
                Location = new System.Drawing.Point(200, 150),
                Width = 150,
                Height = 40
            };
            btnPrintList.Click += (s, e) =>
            {
                txtOutput.Text = controller.PrintList();
            };

            // Botón para imprimir la lista en orden inverso
            btnPrintReverse = new Button
            {
                Text = "Imprimir Inverso",
                Location = new System.Drawing.Point(20, 210),
                Width = 150,
                Height = 40
            };
            btnPrintReverse.Click += (s, e) =>
            {
                txtOutput.Text = controller.PrintReverse();
            };

            // Etiqueta para la salida
            lblOutput = new Label
            {
                Text = "Salida:",
                Location = new System.Drawing.Point(20, 270),
                AutoSize = true
            };

            // Cuadro de texto para mostrar la salida
            txtOutput = new TextBox
            {
                Location = new System.Drawing.Point(20, 300),
                Width = 400,
                Height = 60,
                Multiline = true,
                ReadOnly = true
            };

            // Agregar controles al formulario
            this.Controls.Add(lblInstructions);
            this.Controls.Add(txtValue);
            this.Controls.Add(btnAddToEnd);
            this.Controls.Add(btnAddToStart);
            this.Controls.Add(btnRemove);
            this.Controls.Add(btnPrintList);
            this.Controls.Add(btnPrintReverse);
            this.Controls.Add(lblOutput);
            this.Controls.Add(txtOutput);
        }
    }
}