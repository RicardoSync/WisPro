from customtkinter import CTkFrame, CTkEntry, CTkButton, CTkToplevel
from tkinter import messagebox, ttk, END

from bk_recursos import colores_ui
from bk_consultas import consultarPagos

colores = colores_ui()
pagos = consultarPagos()

def barraBusqueda(daniela):
    frameBusqueda = CTkFrame(daniela, border_color=colores["marcos"], border_width=2,
                            corner_radius=10, fg_color=colores["fondo"]
                            )
    
    nombreID = CTkEntry(frameBusqueda, border_color=colores["marcos"], border_width=2,
                        corner_radius=10, width=420,
                        placeholder_text="Nombre del cliente o ID")
    
    btnBuscarNombre = CTkButton(frameBusqueda, text="Buscar Nombre", border_color=colores["marcos"],
                                border_width=2, corner_radius=10, fg_color=colores["boton"],
                                width=200,
                                text_color="black"
                                )

    btnBuscarID = CTkButton(frameBusqueda, text="Buscar ID", border_color=colores["marcos"],
                                border_width=2, corner_radius=10, fg_color=colores["boton"],
                                width=200,
                                text_color="black"
                                )
    

    frameBusqueda.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    nombreID.grid(column=0, row=0, padx=10, pady=20)
    btnBuscarNombre.grid(column=1, row=0, padx=10, pady=20)
    btnBuscarID.grid(column=2, row=0, padx=10, pady=20)

def moduloPagos():
    daniela = CTkToplevel()
    daniela.title("Pagos")
    daniela.geometry("1000x700")
    daniela.resizable(False, False)
    daniela._set_appearance_mode("dark")


    contenedorTabla = CTkFrame(daniela, border_color=colores["marcos"], border_width=2,
                            corner_radius=10, fg_color="transparent")
    
    tablaPagos = ttk.Treeview(contenedorTabla, columns=("Id Cliente", "Monto", "Fecha", "Metodo"), show="headings")
    tablaPagos.heading("Id Cliente", text="Id Cliente")
    tablaPagos.heading("Monto", text="Monto")
    tablaPagos.heading("Fecha", text="Fecha")
    tablaPagos.heading("Metodo", text="Metodo")

    for item in tablaPagos.get_children():
        tablaPagos.delete(item)
    
    for pago in pagos:
        tablaPagos.insert("", END, values=pago)
    
    #posicion del elemento
    contenedorTabla.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
    tablaPagos.pack(expand=True, fill="both")
    barraBusqueda(daniela)
    daniela.mainloop()


moduloPagos()