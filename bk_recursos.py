from PIL import Image
from customtkinter import CTkImage


def colores_ui():
    colores = {
        "banner": "#D0D8DE",
        "boton": "#94B4CC",
        "marcos": "#3862A1",
        "fondo":   "#181F2A"
    }
    return colores

def imagenes_ui():
    imagenes = {
        "torre" : CTkImage(dark_image=Image.open("img/antena.jpg"),
                        light_image=Image.open("img/antena.jpg"),
                        size=(700,800))
    }
    return imagenes
