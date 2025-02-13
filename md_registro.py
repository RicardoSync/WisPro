from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from bk_recursos import colores_ui, imagenes_ui

iconos = imagenes_ui()
colores = colores_ui()

def md_registro_windows():
    windows = CTk()
    windows.title("Creación de Cuenta")
    windows.geometry("1280x800")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    
    #frame con las opciones

    windows.mainloop()
