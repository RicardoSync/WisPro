from customtkinter import CTkToplevel, CTkFrame, CTkLabel
from tkinter import ttk, END
from bk_recursos import colores_ui, imagenes_ui
from bk_consultas import consultarPagoID

colores = colores_ui()
iconos = imagenes_ui()

def insetarElementos(tablaPagos, idCliente):

    pagos = consultarPagoID(idCliente)
    for item in tablaPagos.get_children():
        tablaPagos.delete(item)
    
    for historial_pagos in pagos:
        tablaPagos.insert('', END, values=historial_pagos)


def obtener_detalles_windows(id_cliente, nombre):

    panel = CTkToplevel()
    panel.title(f"Detalles pagos de {nombre}")
    panel.geometry("1200x600")
    panel.resizable(False, False)

    #creamos el frame
    contenedor = CTkFrame(panel, border_color=colores["marcos"],
                        border_width=2, corner_radius=0,
                        fg_color=colores["fondo"],
                        )
    icono = CTkLabel(contenedor, text="", image=iconos["pago"])


    contenedorTabla = CTkFrame(panel, border_color=colores["marcos"],
                            border_width=2, corner_radius=0,
                            )
    
    tablaPagos = ttk.Treeview(contenedorTabla, columns=("Id Cliente", "Nombre", "Monto", "Fecha", "Metodo"), show="headings")
    tablaPagos.heading("Id Cliente", text="Id Cliente")
    tablaPagos.heading("Nombre", text="Nombre")
    tablaPagos.heading("Monto", text="Monto")
    tablaPagos.heading("Fecha", text="Fecha")
    tablaPagos.heading("Metodo", text="Metodo")


    #posiocin elemento
    contenedor.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    icono.pack(padx=10, pady=10)
    contenedorTabla.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tablaPagos.pack(expand=True, fill="both")
    insetarElementos(tablaPagos, id_cliente)
    panel.mainloop()