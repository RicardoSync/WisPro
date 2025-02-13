from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkImage, CTkOptionMenu
from datetime import datetime
from tkinter import ttk, END, messagebox, Menu
import webbrowser
from PIL import Image

#cargamos los modulos
from bk_update import actualizar_suspencion, actualizar_cancelacion
from bk_recursos import imagenes_ui, colores_ui
from bk_consultas import consultarClientes, detalles_cliente
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
from md_reportar_falla import reportar_falla_windows, reportar_falla_windows_cliente
from md_usuarios import creacionUsuarios
from md_microtik import modulo_microtik
from md_block import panel_bloqueo
from md_detalles_cliente import detalles_cliente
from md_bloqueo_desbloqueo import modulo_bloqueo_desbloqueo
from md_pruebas_red import md_enviar_ping
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
    paquete = identificador[7]

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

def enviarPago(tablaClientes, nombre_admin):
    seleccion = tablaClientes.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "No podemos registrar un pago sin seleccionar un cliente")
        return 
    
    identificado = tablaClientes.item(seleccion, "values")

    id_cliente = identificado[0]
    nombre = identificado[1]
    paquete = identificado[7]
    registar_pago(id_cliente, nombre, paquete, nombre_admin)

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

    # Limpiar la tabla antes de insertar nuevos datos
    for item in tablaClientes.get_children():
        tablaClientes.delete(item)
    
    # Insertar nuevos datos con el tag adecuado
    for cliente in datosClientes:
        estado = cliente[6]  # Suponiendo que el estado está en la columna 7 (índice 6)

        # Aplicar el tag correspondiente según el estado
        if estado == "Activo":
            tag = "Activo"
        elif estado == "Suspendido":
            tag = "Suspendido"
        elif estado == "Bloqueado":
            tag = "Bloqueado"
        elif estado == "Cancelado":
            tag = "Cancelado"
        else:
            tag = ""  # Si el estado no coincide, sin estilo

        tablaClientes.insert("", END, values=cliente, tags=(tag,))

def enviar_bloqueo(tablaClientes):
    seleccion = tablaClientes.selection()
    if not seleccion:
        messagebox.showwarning("SpiderNet", "Para bloquear o desbloquear selecciona un cliente")
        return
    
    identificador = tablaClientes.item(seleccion, "values")
    id_cliente = identificador[0]
    nombre = identificador[1]
    panel_bloqueo(nombreCliente=nombre, id=id_cliente)

def enviar_reporte_falla(rol, tablaClientes):
    selection = tablaClientes.selection()

    if not selection:
        messagebox.showwarning("SpiderNet", "No podemos reportar si no selecciona un cliente")
        return
    
    identificador = tablaClientes.item(selection, "values")

    reportar_falla_windows_cliente(nombre_cliente=identificador[1], rol=rol)

def enviar_suspencion(tablaClientes):
    seleccion = tablaClientes.selection()

    if not seleccion:
        messagebox.showwarning("SpiderNet", "Selecciona un cliente para poder suspenderlo")
        return
    
    identificador = tablaClientes.item(seleccion, "values")
    id_cliente = identificador[0]

    suspender = actualizar_suspencion(id=id_cliente)
    if suspender:
        insertarElementos(tablaClientes)
    else:
        messagebox.showerror("SpiderNet", "No podemos suspender al usuario, verifica el log")

def enviar_cancelacion(tablaClientes):
    seleccion = tablaClientes.selection()

    if not seleccion:
        messagebox.showwarning("SpiderNet", "Selecciona un cliente para poder suspenderlo")
        return
    
    identificador = tablaClientes.item(seleccion, "values")
    id_cliente = identificador[0]

    suspender = actualizar_cancelacion(id=id_cliente)
    if suspender:
        insertarElementos(tablaClientes)
    else:
        messagebox.showerror("SpiderNet", "No podemos cancelar al usuario, verifica el log")

def contenedorTabla(panel, nombre_admin, rol):

    contenedorTable = CTkFrame(panel, border_width=2, corner_radius=0, fg_color=colores["fondo"],
                    border_color=colores["marcos"])
    
    columnas =("ID", "Nombre", "Telefono", "Dia Corte", "Direccion", "Instalacion", "Estado", "Paquete")

    tablaClientes = ttk.Treeview(contenedorTable, columns=columnas, show="headings")
    for col in columnas:
        tablaClientes.heading(col, text=col)


    tablaClientes.column("ID", width=30)
    tablaClientes.column("Instalacion", width=100)

    # Configurar las etiquetas de estilo
    tablaClientes.tag_configure("Activo", background="lightgreen")
    tablaClientes.tag_configure("Suspendido", background="lightcoral")
    tablaClientes.tag_configure("Bloqueado", background="lightgray")
    tablaClientes.tag_configure("Cancelado", background="red")


    #posicion elementos
    contenedorTable.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tablaClientes.pack(expand=True, fill="both")


    #creacion del menu contextual
    menu = Menu(tablaClientes, tearoff=0)
    menu.add_command(label="Crear Cliente", command=nuevoCliente)
    menu.add_command(label="Editar", command=lambda:enviarActualizacion(tablaClientes, panel))
    menu.add_command(label="Eliminar", command=lambda:enviarEliminar(tablaClientes, panel))
    menu.add_command(label="Asignar Equipo", command=lambda:asignacion_equipo(tablaClientes))
    menu.add_command(label="Equipos Instalados", command=lambda:obtenerAsignacion(tablaClientes))
    menu.add_command(label="Registrar Pago", command=lambda:enviarPago(tablaClientes, nombre_admin))
    menu.add_command(label="Historial Pagos", command=lambda:enviarDetalles(tablaClientes))
    menu.add_command(label="Bloquear / Desbloquear cliente", command=lambda:enviar_bloqueo(tablaClientes))
    menu.add_command(label="Suspender", command=lambda:enviar_suspencion(tablaClientes))
    menu.add_command(label="Cancelar servicio", command=lambda:enviar_cancelacion(tablaClientes))
    menu.add_command(label="Reportar falla", command=lambda:enviar_reporte_falla(rol, tablaClientes))
    menu.add_command(label="Actualizar", command=lambda:contenedorTabla(panel, nombre_admin, rol))

    def mostrar_menu(event):
        seleccion = tablaClientes.selection()
        #if seleccion:  # Solo mostrar menú si hay un ítem seleccionado
        menu.post(event.x_root, event.y_root)

    tablaClientes.bind("<Button-3>", mostrar_menu)  # Evento clic derecho


    insertarElementos(tablaClientes)

def enviar_detalles(tablaClientes):
    selecition = tablaClientes.selection()

    if not selecition:
        messagebox.showwarning("SpiderNet", "Por favor selecciona primero un cliente")
        return
    
    identificador = tablaClientes.item(selecition, "values")
    datos = detalles_cliente(id=identificador[0])

    if datos:
        id = identificador[0]
        nombre = identificador[1]
        telefono = identificador[2]
        email = identificador[3]
        direccion = identificador[4]
        fechaRegistro = identificador[5]
        paquete = identificador[6]
        ipCliente = datos[0]
        diaCorte = datos[1]
        detalles_cliente(id, nombre, telefono, email, direccion, fechaRegistro, ipPaquete=paquete, ipCliente=ipCliente, diaCorte=diaCorte)

def panelAdmin(username, rol, windows):
    windows.destroy()
    panel = CTk()
    panel.title(f"Panel de control {username}")
    panel.geometry("1280x800")
    panel.configure(fg_color=colores["fondo"])

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
    
    btnBloqueos =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Bloqueos / Activaciones",
                            text_color="black",
                            command=modulo_bloqueo_desbloqueo
                            )    
    
    btnPagos =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Pagos",
                            text_color="black",
                            command=moduloPagos
                            )
    
    btnGenerarFalla =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Reportar Falla",
                            text_color="black",
                            command=lambda:reportar_falla_windows(rol)
                            )
    
    btnHerramientasRed = CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Pruebas de RED",
                            text_color="black",
                            command=md_enviar_ping
                            )


    btnUsuarios =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Usuarios",
                            text_color="black",
                            command=creacionUsuarios
                            )

    btnContacto =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Informacion",
                            text_color="black",
                            command=lambda:webbrowser.open("https://youtube.com/@tecnoflowz4850?si=V1hMUfxIdD5QAR4Q")
                            )

    btnMicrotik =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Microtik",
                            text_color="black",
                            command=modulo_microtik
                            )

    btnCancelar =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Cancelar",
                            text_color="black",
                            command=panel.destroy
                            )

    informacionLabel = CTkLabel(banner, text="Software Escobedo", text_color="black",
                                font=("Arial", 15, "bold"))
    
    #posicion de los elementos 
    banner.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    logo.pack(padx=10, pady=10)
    welcome.pack(padx=10, pady=10)
    fechaLabel.pack(padx=10, pady=10)
    btnClientes.pack(padx=10, pady=10)
    btnPaquetes.pack(padx=10, pady=10)
    btnEquipos.pack(padx=10, pady=10)
    btnPagos.pack(padx=10, pady=10)
    btnBloqueos.pack(padx=10, pady=10)
    btnGenerarFalla.pack(padx=10, pady=10)
    btnMicrotik.pack(padx=10, pady=10)
    btnHerramientasRed.pack(padx=10, pady=10)
    btnUsuarios.pack(padx=10, pady=10)
    btnContacto.pack(padx=10, pady=10)
    btnCancelar.pack(padx=10, pady=10)
    informacionLabel.pack(padx=10, pady=10)


    contenedorTabla(panel, nombre_admin=username, rol=rol)
    panel.mainloop()