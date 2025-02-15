import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bk_delete import eliminarCliente
from md_actualizar_cliente import actualizarCliente

# Función para crear la ventana de detalles del cliente
def mostrar_detalles_cliente(nombre, id_cliente, telefono, email, direccion, dia_corte, paquete, ip):
    # Extraer los detalles del cliente
    
    # Crear la ventana
    ventana = tk.Toplevel()
    ventana.title(nombre)  # El nombre de la ventana será el nombre del cliente
    ventana.geometry("400x400")  # Tamaño de la ventana
    ventana.config(bg="#f0f0f0")  # Color de fondo
    
    # Crear un marco para los detalles
    marco = tk.Frame(ventana, bg="#f0f0f0")
    marco.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    
    # Crear el Treeview (tabla) para los detalles del cliente
    tree = ttk.Treeview(marco, columns=("Detalle", "Valor"), show="headings", height=7)
    tree.heading("Detalle", text="Detalle", anchor=tk.W)
    tree.heading("Valor", text="Valor", anchor=tk.W)
    
    # Configuración de columnas
    tree.column("Detalle", width=100, anchor=tk.W)
    tree.column("Valor", width=250, anchor=tk.W)
    
    # Insertar los detalles del cliente en la tabla
    tree.insert("", tk.END, values=("ID Cliente", id_cliente))
    tree.insert("", tk.END, values=("Nombre", nombre))
    tree.insert("", tk.END, values=("Teléfono", telefono))
    tree.insert("", tk.END, values=("Email", email))
    tree.insert("", tk.END, values=("Dirección", direccion))
    tree.insert("", tk.END, values=("IP", ip))
    tree.insert("", tk.END, values=("Día de Corte", dia_corte))
    tree.insert("", tk.END, values=("Paquete", paquete))
    
    tree.pack(padx=10, pady=10)
    
    # Funciones para los botones
    def editar_cliente():
        ventana.destroy()
        actualizarCliente(id_cliente, nombre, telefono, email, direccion, paquete, ip, dia_corte)
    def eliminar_cliente():
        respuesta = messagebox.askyesno("Eliminar", "¿Estás seguro de eliminar este cliente?")
        if respuesta:
            eliminarCliente(id_cliente)
            messagebox.showinfo("Eliminar", "Cliente eliminado correctamente.")
            ventana.destroy()

    def cancelar():
        ventana.destroy()
    
    # Crear un marco para los botones
    marco_botones = tk.Frame(ventana, bg="#f0f0f0")
    marco_botones.pack(pady=20)
    
    # Botones
    boton_editar = tk.Button(marco_botones, text="Editar", command=editar_cliente, bg="#4CAF50", fg="white", width=12, relief="flat", font=("Arial", 10, "bold"))
    boton_editar.grid(row=0, column=0, padx=10, pady=5)

    boton_eliminar = tk.Button(marco_botones, text="Eliminar", command=eliminar_cliente, bg="#FF6347", fg="white", width=12, relief="flat", font=("Arial", 10, "bold"))
    boton_eliminar.grid(row=0, column=1, padx=10, pady=5)

    boton_cancelar = tk.Button(marco_botones, text="Cancelar", command=cancelar, bg="#888888", fg="white", width=12, relief="flat", font=("Arial", 10, "bold"))
    boton_cancelar.grid(row=0, column=2, padx=10, pady=5)

    # Ejecutar la ventana
    ventana.mainloop()

