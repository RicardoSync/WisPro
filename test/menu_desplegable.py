from customtkinter import CTk, CTkOptionMenu, CTkFrame
from bk_recursos import colores_ui
colores = colores_ui()

def seleccionar_opcion(valor):
    print(f"Seleccionaste: {valor}")  # Puedes cambiar esto por otra acción

def panelAdmin(username, rol, windows):
    panel = CTk()
    panel.title(f"Panel de control {username}")
    panel.geometry("1280x800")
    panel.configure(fg_color=colores["fondo"])

    # Crear el panel lateral
    banner = CTkFrame(panel, border_width=2, corner_radius=0, fg_color=colores["fondo"],
                      border_color=colores["marcos"])

    # Menú desplegable
    opciones = ["Clientes", "Paquetes", "Equipos", "Pagos", "Configuración"]
    menu_desplegable = CTkOptionMenu(banner, values=opciones, command=seleccionar_opcion)
    menu_desplegable.pack(padx=10, pady=10)

    # Resto de la UI...
    
    banner.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    
    panel.mainloop()


panelAdmin(username="ricardo", rol=0, windows=None)