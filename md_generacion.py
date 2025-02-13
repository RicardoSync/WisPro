from customtkinter import CTkToplevel, CTkLabel, CTkEntry, CTkButton
from tkinter import messagebox
from bk_recursos import colores_ui


colores = colores_ui()


def generacion_sistema():
    windows = CTkToplevel()
    windows.title("Generacion de Datos")
    windows.geometry("700x500")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])



    windows.mainloop()


generacion_sistema()