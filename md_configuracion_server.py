from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel
from bk_recursos import colores_ui
import json

colores = colores_ui()

def md_configurar_mysql():
    windows = CTk()
    windows.title("Configurar Servidor")
    windows.geometry("800x600")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    hostEntry = CTkEntry(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        )

    windows.mainloop()


md_configurar_mysql()