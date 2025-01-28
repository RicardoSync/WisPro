from PIL import Image
from customtkinter import CTkImage

def imagenes_ui():
    imagenes = {
        "logo": CTkImage(light_image=Image.open("img/logo.png"),
                        dark_image=Image.open("img/logo.png"),
                        size=(150,150)),

        "cliente": CTkImage(light_image=Image.open("img/cliente.png"),
                        dark_image=Image.open("img/cliente.png"),
                        size=(150,150)),
        
        "pago": CTkImage(light_image=Image.open("img/pago.png"),
                        dark_image=Image.open("img/pago.png"),
                        size=(150, 150))
    }
    return imagenes

def colores_ui():
    colores = {
        "fondo": "#58595E",
        "marcos": "#D0D0D0",
        "boton" : "#ABACB0"
    }
    return colores