from customtkinter import CTk, CTkEntry, CTkButton, CTkFrame, CTkLabel, CTkTabview
from datetime import datetime

#recursos
from bk_recursos import colores_ui
colores = colores_ui()



def panelAdministracion(username, rol, ventana):
    windows = CTk()
    windows.title(f"Panel de control {username}")
    windows.geometry("1280x800")
    windows.resizable(False, False)
    windows._set_appearance_mode("dark")
    fecha = datetime.now().strftime("%d/%m/%Y")

    #creacion del banner
    banner = CTkFrame(windows, border_color=colores["marcos"], border_width=2,
                    corner_radius=0,
                    fg_color="transparent")
    
    welcome = CTkLabel(banner, text=f"Bienvenido de nuevo! {username}", 
                        font=("Monospace", 20),
                        text_color="white"
                        )
    
    fechaLabel = CTkLabel(banner, text=f"Fecha: {fecha}",
                        font=("Monospace", 20),
                        text_color="white")
    
    infomarcion = CTkLabel(banner, text="Tipo Usuario: Administrador",
                        font=("Monospace", 15),
                        text_color="white"
                        )

    #creacion del tambview
    tabView = CTkTabview(windows, border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        fg_color="transparent"
                        )
    
    tabView.add("Home")
    tabView.add("Paquetes")
    tabView.add("Clientes")
    tabView.add("Asignacion Equipos")
    tabView.add("Mantenimiento")

    #posicion de los elementos
    banner.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    welcome.place(relx=0.02, rely=0.1)
    fechaLabel.place(relx=0.83, rely=0.1)
    infomarcion.place(relx=0.02, rely=0.5)

    tabView.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
    windows.mainloop()