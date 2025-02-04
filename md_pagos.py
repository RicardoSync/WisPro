from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkToplevel
from tkinter import messagebox, ttk, END, Menu

from bk_recursos import colores_ui
from bk_consultas import consultarPagos, consultarPagoNombre, consultarPagoID
from md_registro_pago import registar_pago

colores = colores_ui()

def enviar_detalles(tablaPagos):
    seleccionado = tablaPagos.selection()

    if not seleccionado:
        messagebox.showerror("SpiderNet", "No podemos obtener detalles si no hay nada seleccionado")
        return
    identificador = tablaPagos.item(seleccionado, "values")
    print(identificador)

def actualizar_tabla(tablaPagos):
    """Consulta la base de datos y actualiza la tabla con los nuevos datos."""
    pagos_actualizados = consultarPagos()
    insertarElementos(tablaPagos, pagos_actualizados)

def enviarBusqueda(tablaPagos, nombreID, busquedaPor):
    valorBusqueda = nombreID.get()
    if not valorBusqueda:
        messagebox.showerror("SpiderNet", "No podemos buscar un campo vacío")
        return

    if busquedaPor == "nombre":
        pagosBusqueda = consultarPagoNombre(valorBusqueda)
    else:  # Búsqueda por ID
        if not valorBusqueda.isdigit():
            messagebox.showerror("SpiderNet", "El ID debe ser un número")
            return
        pagosBusqueda = consultarPagoID(int(valorBusqueda))

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
                        corner_radius=10, width=420, placeholder_text="Nombre del cliente o ID")
    
    btnBuscarNombre = CTkButton(frameBusqueda, text="Buscar Nombre", border_color=colores["marcos"],
                                border_width=2, corner_radius=10, fg_color=colores["boton"],
                                width=200, text_color="black",
                                command=lambda: enviarBusqueda(tablaPagos, nombreID, "nombre"))
    
    btnBuscarID = CTkButton(frameBusqueda, text="Buscar ID", border_color=colores["marcos"],
                            border_width=2, corner_radius=10, fg_color=colores["boton"],
                            width=200, text_color="black",
                            command=lambda: enviarBusqueda(tablaPagos, nombreID, "id"))

    frameBusqueda.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    nombreID.grid(column=0, row=0, padx=10, pady=20)
    btnBuscarNombre.grid(column=1, row=0, padx=10, pady=20)
    btnBuscarID.grid(column=2, row=0, padx=10, pady=20)

def tablaPagos(ventana, pagos):
    contenedorTabla = CTkFrame(ventana, border_color=colores["marcos"], border_width=2,
                                corner_radius=10, fg_color="transparent")

    tabla = ttk.Treeview(contenedorTabla, columns=("Id Cliente", "Nombre", "Monto", "Fecha", "Metodo"), show="headings")
    tabla.heading("Id Cliente", text="Id Cliente")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Monto", text="Monto")
    tabla.heading("Fecha", text="Fecha")
    tabla.heading("Metodo", text="Metodo")

    contenedorTabla.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
    insertarElementos(tabla, pagos)  # Pasamos los pagos al inicio
    tabla.pack(expand=True, fill="both")


    #creacion del menu contextual
    menu = Menu(tabla, tearoff=0)
    menu.add_command(label="Actualizar", command=lambda:actualizar_tabla(tabla))


    def mostrar_menu(event):
        seleccion = tabla.selection()
        menu.post(event.x_root, event.y_root)

    tabla.bind("<Button-3>", mostrar_menu)  # Evento clic derecho

    return tabla

def moduloPagos():
    ventana = CTkToplevel()
    ventana.title("Pagos")
    ventana.geometry("1000x700")
    ventana.resizable(False, False)
    pagos = consultarPagos()

    tabla = tablaPagos(ventana, pagos)  # Guardamos la referencia a la tabla
    barraBusqueda(tabla, ventana)  # Pasamos la tabla correctamente

    ventana.mainloop()
