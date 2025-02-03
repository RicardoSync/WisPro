import tkinter as tk
from tkinter import ttk

# Crear ventana
root = tk.Tk()
root.title("Tabla con colores")

# Crear Treeview
columns = ("ID", "Nombre", "Estado")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Definir encabezados
for col in columns:
    tree.heading(col, text=col)

# Configurar etiquetas (tags) para cada estado
tree.tag_configure("activo", foreground="green")
tree.tag_configure("bloqueado", foreground="orange")
tree.tag_configure("cancelado", foreground="red")

# Datos de prueba
clientes = [
    (1, "Juan", "Bloqueado"),
    (2, "Pedro", "Bloqueado"),
    (3, "Ana", "Cancelado"),
    (4, "Carlos", "Activo"),
]

# Agregar filas con el color correspondiente
for cliente in clientes:
    id_cliente, nombre, estado = cliente
    tag = estado.lower()  # Convertir a minúsculas para coincidir con los tags
    tree.insert("", "end", values=cliente, tags=(tag,))

# Empaquetar Treeview
tree.pack(expand=True, fill="both")

# Iniciar aplicación
root.mainloop()
