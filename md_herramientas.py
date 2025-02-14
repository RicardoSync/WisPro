from md_pruebas_red import md_enviar_ping
from generar_clientes import md_generacion
from customtkinter import CTkToplevel, CTkLabel, CTkButton
from bk_recursos import colores_ui, imagenes_ui


iconos = imagenes_ui()
colores = colores_ui()

def md_herramentas():
    windows = CTkToplevel()
    windows.title("Herramientas del Sitema")
    windows.geometry("700x600")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])


    btnPing = CTkButton(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Ping", text_color="black",
                        image=iconos["ping"],
                        command=md_enviar_ping)
    
    btnGeneracion = CTkButton(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Generar Datos", text_color="black",
                        image=iconos["auto"],
                        command=md_generacion)
    

    btnPing.grid(column=0, row=0, padx=10, pady=10)
    btnGeneracion.grid(column=1, row=0, padx=10, pady=10)

    windows.mainloop()

