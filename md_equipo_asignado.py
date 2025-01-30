from customtkinter import CTkToplevel, CTkFrame, CTkLabel
from tkinter import ttk, END, Menu
from bk_recursos import colores_ui, imagenes_ui
from bk_consultas import consultarEquipoID

colores = colores_ui()
iconos = imagenes_ui()

def insetarElementos(tablaEquipos, idCliente):

    pagos = consultarEquipoID(idCliente)
    for item in tablaEquipos.get_children():
        tablaEquipos.delete(item)
    
    for historial_pagos in pagos:
        tablaEquipos.insert('', END, values=historial_pagos)


def obtener_detalles_equipo(id_cliente, nombre):

    panel = CTkToplevel()
    panel.title(f"Equipo asignado de {nombre}")
    panel.geometry("1200x600")
    panel.resizable(False, False)
    panel._set_appearance_mode("dark")

    #creamos el frame
    contenedor = CTkFrame(panel, border_color=colores["marcos"],
                        border_width=2, corner_radius=0,
                        fg_color=colores["fondo"],
                        )
    icono = CTkLabel(contenedor, text="", image=iconos["equipo"])


    contenedorTabla = CTkFrame(panel, border_color=colores["marcos"],
                            border_width=2, corner_radius=0,
                            )
    
    tablaEquipos = ttk.Treeview(contenedorTabla, columns=("Id", "Nombre", "Tipo", "Modelo", "Estado", "Id cliente"), show="headings")
    tablaEquipos.heading("Id", text="Id")
    tablaEquipos.heading("Nombre", text="Nombre")
    tablaEquipos.heading("Tipo", text="Tipo")
    tablaEquipos.heading("Modelo", text="Modelo")
    tablaEquipos.heading("Estado", text="Estado")
    tablaEquipos.heading("Id cliente", text="Id cliente")

    #creacion del menu contextual
    menu = Menu(tablaEquipos, tearoff=0)
    menu.add_command(label="Editar")
    menu.add_command(label="Actualizar", command=lambda:contenedorTabla(panel))

    def mostrar_menu(event):
        seleccion = tablaEquipos.selection()
        if seleccion:  # Solo mostrar menú si hay un ítem seleccionado
            menu.post(event.x_root, event.y_root)

    tablaEquipos.bind("<Button-3>", mostrar_menu)  # Evento clic derecho

    #posiocin elemento
    contenedor.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    icono.pack(padx=10, pady=10)
    contenedorTabla.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tablaEquipos.pack(expand=True, fill="both")
    insetarElementos(tablaEquipos, id_cliente)
    panel.mainloop()