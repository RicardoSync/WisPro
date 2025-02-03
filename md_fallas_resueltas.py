from customtkinter import CTkFrame, CTkButton, CTkToplevel
from tkinter import ttk, END, Menu, messagebox
from bk_consultas import listar_fallas_resueltas  
from bk_recursos import colores_ui

colores = colores_ui()

def insertarElementosFallas(tablaFallas, fallas):
    """Elimina todos los elementos de la tabla y la actualiza con las fallas resueltas."""
    for item in tablaFallas.get_children():
        tablaFallas.delete(item)

    for falla in fallas:
        tablaFallas.insert("", END, values=falla)

def actualizar_tabla_fallas(tablaFallas):
    """Consulta las fallas resueltas y actualiza la tabla."""
    fallas_actualizadas = listar_fallas_resueltas()
    insertarElementosFallas(tablaFallas, fallas_actualizadas)

def tablaFallasResueltas(ventana):
    """Crea y configura la tabla para mostrar las fallas resueltas."""
    contenedorTabla = CTkFrame(ventana, border_color=colores["marcos"], border_width=2,
                               corner_radius=10, fg_color=colores["fondo"])

    columnas = ("id_cliente", "nombre_cliente", "tipo_falla", "descripcion",
                "estado", "fecha_reporte", "fecha_reparacion", "id_usuario", "nombre_usuario")

    tabla = ttk.Treeview(contenedorTabla, columns=columnas, show="headings", height=15)

    # Definir encabezados
    encabezados = {
        "id_cliente": "ID Cliente", "nombre_cliente": "Cliente",
        "tipo_falla": "Tipo de Falla", "descripcion": "Descripción",
        "estado": "Estado", "fecha_reporte": "Fecha de Reporte",
        "fecha_reparacion": "Fecha de Reparación", "id_usuario": "ID Usuario",
        "nombre_usuario": "Usuario"
    }
    
    for col in columnas:
        tabla.heading(col, text=encabezados[col], anchor="center")
        tabla.column(col, anchor="center", stretch=True)

    contenedorTabla.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.7)
    insertarElementosFallas(tabla, listar_fallas_resueltas())  
    tabla.pack(expand=True, fill="both", padx=10, pady=10)

    # Menú contextual (clic derecho)
    menu = Menu(tabla, tearoff=0, bg=colores["fondo-xp"], fg="black", activebackground=colores["boton"])
    menu.add_command(label="Actualizar", command=lambda: actualizar_tabla_fallas(tabla))

    def mostrar_menu(event):
        seleccion = tabla.selection()
        if seleccion:
            menu.post(event.x_root, event.y_root)

    tabla.bind("<Button-3>", mostrar_menu)

    return tabla

def moduloFallasResueltas():
    """Crea la ventana para mostrar las fallas resueltas con mejor diseño."""
    ventana = CTkToplevel()
    ventana.title("Fallas Resueltas")
    ventana.geometry("1200x700")
    ventana.configure(fg_color=colores["fondo"])

    titulo = CTkFrame(ventana, fg_color=colores["fondo"], height=50)
    titulo.pack(fill="x", padx=10, pady=5)

    tabla = tablaFallasResueltas(ventana)

    # Botón de actualización con más estilo
    btnActualizar = CTkButton(ventana, text="Actualizar", border_color=colores["marcos"],
                              border_width=2, corner_radius=10, fg_color=colores["boton"],
                              text_color="black", width=180,
                              font=("Arial", 14, "bold"),
                              command=lambda: actualizar_tabla_fallas(tabla))
    btnActualizar.place(relx=0.4, rely=0.85, relwidth=0.2)

    ventana.mainloop()

