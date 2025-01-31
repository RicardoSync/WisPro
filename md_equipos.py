from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkToplevel
from tkinter import messagebox, ttk, END, Menu

from bk_recursos import colores_ui
from bk_consultas import consultarEquipoNombre, consultarEquipoID, consultarEquipos, consutarEquiposActualizacion
from md_actualizar_equipo import editar_equipo_windows
from bk_delete import eliminarEquipo

colores = colores_ui()
pagos = consultarEquipos()


def enviarEliminacion(tabla):
    seleccion = tabla.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "Primero selecciona un elemento")
    
    identificador = tabla.item(seleccion, "values")
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

def actualizar_tabla(tablaPagos):
    """Consulta la base de datos y actualiza la tabla con los nuevos datos."""
    pagos_actualizados = consultarEquipos()

    insertarElementos(tablaPagos, pagos_actualizados)

def enviarBusqueda(tablaPagos, nombreID, busquedaPor):
    valorBusqueda = nombreID.get()
    if not valorBusqueda:
        messagebox.showerror("SpiderNet", "No podemos buscar un campo vacío")
        return

    if busquedaPor == "nombre":
        pagosBusqueda = consultarEquipoNombre(valorBusqueda)
    else:  # Búsqueda por ID
        if not valorBusqueda.isdigit():
            messagebox.showerror("SpiderNet", "El ID debe ser un número")
            return
        pagosBusqueda = consultarEquipoID(int(valorBusqueda))

    insertarElementos(tablaPagos, pagosBusqueda)

def insertarElementos(tablaPagos, pagosBusqueda):
    for item in tablaPagos.get_children():
        tablaPagos.delete(item)

    for pago in pagosBusqueda:
        tablaPagos.insert("", END, values=pago)

def barraBusqueda(tablaPagos, ventana):
    frameBusqueda = CTkFrame(ventana, border_color=colores["marcos"], border_width=2,
                            corner_radius=10, fg_color=colores["fondo"])
    
    nombreID = CTkEntry(frameBusqueda, border_color=colores["marcos"], border_width=2,
                        corner_radius=10, width=420, placeholder_text="ID del cliente")
    

    
    btnBuscarID = CTkButton(frameBusqueda, text="Buscar ID", border_color=colores["marcos"],
                            border_width=2, corner_radius=10, fg_color=colores["boton"],
                            width=200, text_color="black",
                            command=lambda: enviarBusqueda(tablaPagos, nombreID, "id"))

    frameBusqueda.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    nombreID.grid(column=0, row=0, padx=10, pady=20)
    btnBuscarID.grid(column=2, row=0, padx=10, pady=20)

def tablaPagos(ventana):
    contenedorTabla = CTkFrame(ventana, border_color=colores["marcos"], border_width=2,
                                corner_radius=10, fg_color="transparent")

    tabla = ttk.Treeview(contenedorTabla, columns=("id", "Nombre", "Tipo", "Marca", "Modelo", "Estado", "id_cliente"), show="headings")
    tabla.heading("id", text="id")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Tipo", text="Tipo")
    tabla.heading("Marca", text="Marca")
    tabla.heading("Modelo", text="Modelo")
    tabla.heading("Estado", text="Estado")
    tabla.heading("id_cliente", text="id_cliente")

    tabla.column("id", width=60)
    tabla.column("id_cliente", width=60)

    contenedorTabla.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
    insertarElementos(tabla, pagos)  # Pasamos los pagos al inicio
    tabla.pack(expand=True, fill="both")


    #creacion del menu contextual
    menu = Menu(tabla, tearoff=0)
    menu.add_command(label="Editar", command=lambda:enviar_actualizacion(tabla))
    menu.add_command(label="Actualizar", command=lambda:actualizar_tabla(tabla))



    def mostrar_menu(event):
        seleccion = tabla.selection()
        menu.post(event.x_root, event.y_root)

    tabla.bind("<Button-3>", mostrar_menu)  # Evento clic derecho

    return tabla

def moduloEquipos():
    ventana = CTkToplevel()
    ventana.title("Equipos")
    ventana.geometry("1200x700")
    ventana.resizable(False, False)
    ventana._set_appearance_mode("dark")

    tabla = tablaPagos(ventana)  # Guardamos la referencia a la tabla
    barraBusqueda(tabla, ventana)  # Pasamos la tabla correctamente
    actualizar_tabla(tabla)
    ventana.mainloop()
