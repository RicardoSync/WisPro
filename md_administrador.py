from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from datetime import datetime

#cargamos los modulos
from bk_recursos import imagenes_ui, colores_ui
from md_usuarios import creacionUsuarios
iconos = imagenes_ui()
colores = colores_ui()
fecha = datetime.now().strftime("%d/%m/%Y")


def panelAdmin(username, rol, windows):
    windows.destroy()

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
    btnPaquetes = CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Paquetes",
                            text_color="black"
                            )
    
    btnEquipos =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Equipos",
                            text_color="black"
                            )
    
    btnPagos =  CTkButton(banner, border_width=2, border_color=colores["marcos"],
                            fg_color=colores["boton"],
                            width=200,
                            text="Pagos",
                            text_color="black"
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
                            text="Configuracion",
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
    btnPaquetes.pack(padx=10, pady=10)
    btnEquipos.pack(padx=10, pady=10)
    btnPagos.pack(padx=10, pady=10)
    btnUsuarios.pack(padx=10, pady=10)
    btnConfiguracion.pack(padx=10, pady=10)
    btnCancelar.pack(padx=10, pady=10)


    panel.mainloop()