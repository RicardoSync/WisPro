from customtkinter import CTkToplevel, CTkFrame, CTkLabel, CTkButton
from tkinter import ttk, END, Menu, messagebox
from bk_recursos import colores_ui, imagenes_ui
from bk_consultas import consultarEquipoID, consutarEquiposActualizacion
from bk_delete import eliminarEquipo
from md_actualizar_equipo import editar_equipo_windows

colores = colores_ui()
iconos = imagenes_ui()

def insetarElementos(tablaEquipos, idCliente):

    pagos = consultarEquipoID(idCliente)
    for item in tablaEquipos.get_children():
        tablaEquipos.delete(item)
    
    for historial_pagos in pagos:
        tablaEquipos.insert('', END, values=historial_pagos)

def enviarEliminacion(tablaEquipos):
    seleccion = tablaEquipos.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "Primero selecciona un elemento")
    
    identificador = tablaEquipos.item(seleccion, "values")
    confirmacion = messagebox.askyesno("SpiderNet", "Deseas elimnar este equipo al cliente? ")

    if confirmacion:
        eliminarEquipo(id=identificador[0])
    else:
        return
        
def enviar_actualizacion(tablaEquupos):
    seleccionado = tablaEquupos.selection()

    if not seleccionado:
        messagebox.showerror("SpiderNet", "Selecciona primero un elemento")
        return
    
    identidicador = tablaEquupos.item(seleccionado, "values")

    datos = consutarEquiposActualizacion(id=identidicador[0])
    id_equipo = identidicador[0] #el id lo obtener directo de la tabla sin consultas
    nombre = datos[0]
    tipo_equipo_obtenido = datos[1]
    marca = datos[2]
    modelo = datos[3]
    mac= datos[4]
    serial = datos[5]
    estado_equipo_obtenido = datos[6]


    editar_equipo_windows(nombre, tipo_equipo_obtenido, marca, modelo, mac, serial, estado_equipo_obtenido, id_equipo)


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
    
    btnCancelar = CTkButton(contenedor, border_color=colores["marcos"], border_width=2,
                            corner_radius=10, fg_color=colores["boton"],
                            text="Cancelar",
                            text_color="black",
                            command=panel.destroy
                            )


    tablaEquipos = ttk.Treeview(contenedorTabla, columns=("Id", "Nombre", "Tipo","Marca", "Modelo", "Estado", "Id cliente"), show="headings")
    tablaEquipos.heading("Id", text="Id")
    tablaEquipos.heading("Nombre", text="Nombre")
    tablaEquipos.heading("Tipo", text="Tipo")
    tablaEquipos.heading("Marca", text="Marca")
    tablaEquipos.heading("Modelo", text="Modelo")
    tablaEquipos.heading("Estado", text="Estado")
    tablaEquipos.heading("Id cliente", text="Id cliente")

    tablaEquipos.column("Id", width=30)
    tablaEquipos.column("Tipo", width=30)
    tablaEquipos.column("Estado", width=30)
    tablaEquipos.column("Id cliente", width=50)

    #creacion del menu contextual
    menu = Menu(tablaEquipos, tearoff=0)
    menu.add_command(label="Editar", command=lambda:enviar_actualizacion(tablaEquipos))
    menu.add_command(label="Eliminar", command=lambda:enviarEliminacion(tablaEquipos))
    menu.add_command(label="Actualizar", command=lambda:insetarElementos(tablaEquipos, id_cliente))

    def mostrar_menu(event):
        seleccion = tablaEquipos.selection()
        if seleccion:  # Solo mostrar menú si hay un ítem seleccionado
            menu.post(event.x_root, event.y_root)

    tablaEquipos.bind("<Button-3>", mostrar_menu)  # Evento clic derecho

    #posiocin elemento
    contenedor.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    icono.pack(padx=10, pady=10)
    btnCancelar.pack(padx=10, pady=10)
    contenedorTabla.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tablaEquipos.pack(expand=True, fill="both")
    insetarElementos(tablaEquipos, id_cliente)
    panel.mainloop()