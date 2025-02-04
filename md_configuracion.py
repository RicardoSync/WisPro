from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkLabel
import json
from bk_recursos import colores_ui

colores = colores_ui()

def panelConfiguracion():
    windows = CTkToplevel()
    windows.title("Cambiar Configuracion")
    windows.resizable