from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from datetime import datetime
from tkinter import ttk, END, messagebox, Menu

#cargamos los modulos
from bk_recursos import imagenes_ui, colores_ui
from bk_consultas import consultarClientes
from md_usuarios import creacionUsuarios
from md_paquetes import creacionPaquetes
from bk_delete import eliminarCliente
from md_nuevo_cliente import nuevoCliente
from md_actualizar_cliente import actualizarCliente
from md_registro_pago import registar_pago
from md_pagos import moduloPagos
from md_asignacin_equipo import asignacionEquipo
from md_equipos import moduloEquipos
from md_histotial_pagos import obtener_detalles_windows
from md_equipo_asignado import obtener_detalles_equipo

iconos = imagenes_ui()
colores = colores_ui()
fecha = datetime.now().strftime("%d/%m/%Y")

def enviarEliminar(tablaClientes, panel):
        seleccionado = tablaClientes.selection()

        if not seleccionado:
            messagebox.showerror("SpiderNet", "No podemos eliminar un cliente sin seleccionar")
            return
        
        identificador = tablaClientes.item(seleccionado, "values")
        
        confirmacion = messagebox.askyesno("SpiderNet", "Deseas eliminar al cliente? ")

        if confirmacion:
            eliminarCliente(id=identificador[0])
            contenedorTabla(panel)

def enviarActualizacion(tablaClientes, panel):
    seleccionado = tablaClientes.selection()

    if not seleccionado:
        messagebox.showerror("SpiderNet", "No podemos actualizar si no esta seleccionado")
        return
    
    identificador = tablaClientes.item(seleccionado, "values")
    
    id_cliente = identificador[0]
    nombre = identificador[1]
    telefono = identificador[2]
    email = identificador[3]
    direccion = identificador[4]
    paquete = identificador[6]

    actualizarCliente(id_cliente, nombre, telefono, email, direccion, paquete)

def asignacion_equipo(tablaClientes):
    seleccionado = tablaClientes.selection()

    if not seleccionado:
        messagebox.showerror("SpiderNet", "No podemos asignar un equipo si no seleccionas un cliente")
        return
    
    identificador = tablaClientes.item(seleccionado, "values")
    id_cliente = identificador[0]
    nombre = identificador[1]

    asignacionEquipo(id_cliente, nombre)

def enviarPago(tablaClientes):
    seleccion = tablaClientes.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "No podemos registrar un pago sin seleccionar un cliente")
        return 
    
    identificado = tablaClientes.item(seleccion, "values")

    id_cliente = identificado[0]
    nombre = identificado[1]
    paquete = identificado[6]
    registar_pago(id_cliente, nombre, paquete)

def enviarDetalles(tablaClientes):
    seleccion = tablaClientes.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "Por favot selecciona un cliente")
    
    identificador = tablaClientes.item(seleccion, "values")
    obtener_detalles_windows(id_cliente=identificador[0], nombre=identificador[1])

def obtenerAsignacion(tablaClientes):
    seleccion = tablaClientes.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "Por favot selecciona un cliente")
    
    identificador = tablaClientes.item(seleccion, "values")
    obtener_detalles_equipo(id_cliente=identificador[0], nombre=identificador[1])

def insertarElementos(tablaClientes):
    datosClientes = consultarClientes()

    for item in tablaClientes.get_children():
        tablaClientes.delete(item)
    
    for clientes in datosClientes:
        tablaClientes.insert("", END, values=clientes)


def contenedorTabla(panel):

    contenedorTable = CTkFrame(panel, border_width=2, corner_radius=0, fg_color=colores["fondo"],
                    border_color=colores["marcos"])
    
    tablaClientes = ttk.Treeview(contenedorTable, columns=("ID", "Nombre", "Telefono", "Email", "Direccion", "Instalacion", "Paquete"), show="headings")
    tablaClientes.heading("ID", text="ID")
    tablaClientes.heading("Nombre", text="Nombre")
    tablaClientes.heading("Telefono", text="Telefono")
    tablaClientes.heading("Email", text="Email")
    tablaClientes.heading("Direccion", text="Direccion")
    tablaClientes.heading("Instalacion", text="Instalacion")
    tablaClientes.heading("Paquete", text="Paquete")

    
    #posicion elementos
    contenedorTable.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tablaClientes.pack(expand=True, fill="both")


    #creacion del menu contextual
    menu = Menu(tablaClientes, tearoff=0)
    menu.add_command(label="Nuevo Cliente", command=nuevoCliente)
    menu.add_command(label="Asignar Equipo", command=lambda:asignacion_equipo(tablaClientes))
    menu.add_command(label="Equipo Asignado", command=lambda:obtenerAsignacion(tablaClientes))
    menu.add_command(label="Editar", command=lambda:enviarActualizacion(tablaClientes, panel))
    menu.add_command(label="Eliminar", command=lambda:enviarEliminar(tablaClientes, panel))
    menu.add_command(label="Registrar Pago", command=lambda:enviarPago(tablaClientes))
    menu.add_command(label="Historial Pagos", command=lambda:enviarDetalles(tablaClientes))
    menu.add_command(label="Actualizar", command=lambda:contenedorTabla(panel))

    def mostrar_menu(event):
        seleccion = tablaClientes.selection()
        #if seleccion:  # Solo mostrar menú si hay un ítem seleccionado
        menu.post(event.x_root, event.y_root)

    tablaClientes.bind("<Button-3>", mostrar_menu)  # Evento clic derecho


    insertarElementos(tablaClientes)

def panelAdmin(username, rol, windows):
    panel = CTk()
    panel.title(f"Panel de control {username}")
    panel.geometry("1280x800")
    panel._set_appearance_mode("dark")

    #creamos el panel
    banner = CTkFrame(panel, border_width=2, corner_radius=0, fg_color=colores["fondo"],
                    border_color=colores["marcos"],
                    )
    
    logo = CTkLabel(banner, text="", image=iconos["logo"])
    welcome = CTkLabel(banner, text=f"Bienvenido {username}", font=("Arial", 20, "bold"),
                    text_color="black")
    
    fechaLabel = CTkLabel(banner, text=f"Fecha: {fecha}", font=("Arial", 18, "bold"),
                    text_color="black")
    
    #creamos los botones

    btnClientes = CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Clientes",
                            text_color="black",
                            command=nuevoCliente
                            )
    
    btnPaquetes = CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Paquetes",
                            text_color="black",
                            command=creacionPaquetes
                            )
    
    btnEquipos =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Equipos",
                            text_color="black",
                            command=moduloEquipos
                            )
    
    btnPagos =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Pagos",
                            text_color="black",
                            command=moduloPagos
                            )
    
    btnUsuarios =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Usuarios",
                            text_color="black",
                            command=creacionUsuarios
                            )
    
    btnConfiguracion =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Herramientas",
                            text_color="black"
                            )

    btnCancelar =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Cancelar",
                            text_color="black",
                            command=panel.destroy
                            )

    #posicion de los elementos 
    banner.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    logo.pack(padx=10, pady=20)
    welcome.pack(padx=10, pady=10)
    fechaLabel.pack(padx=10, pady=10)
    btnClientes.pack(padx=10, pady=10)
    btnPaquetes.pack(padx=10, pady=10)
    btnEquipos.pack(padx=10, pady=10)
    btnPagos.pack(padx=10, pady=10)
    btnUsuarios.pack(padx=10, pady=10)
    btnConfiguracion.pack(padx=10, pady=10)
    btnCancelar.pack(padx=10, pady=10)


    contenedorTabla(panel)
    panel.mainloop()