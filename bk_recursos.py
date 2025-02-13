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
                        size=(150, 150)),
        
        "equipo": CTkImage(light_image=Image.open("img/equipo.png"),
                        dark_image=Image.open("img/equipo.png"),
                        size=(150, 150)),
        
        "usuario": CTkImage(light_image=Image.open("img/usuario.png"),
                        dark_image=Image.open("img/usuario.png"),
                        size=(100, 100)),

        "ticket": CTkImage(light_image=Image.open("img/ticket.png"),
                        dark_image=Image.open("img/ticket.png"),
                        size=(100, 100)),

        "falla": CTkImage(light_image=Image.open("img/falla.png"),
                        dark_image=Image.open("img/falla.png"),
                        size=(100, 100)),


        "solucion": CTkImage(light_image=Image.open("img/solucion.png"),
                        dark_image=Image.open("img/solucion.png"),
                        size=(100, 100)),
        
        "hacker": CTkImage(light_image=Image.open("img/hacker.png"),
                        dark_image=Image.open("img/hacker.png"),
                        size=(150, 150))
    }
    return imagenes

def colores_ui():
    colores = {
        "fondo": "#58595E",
        "marcos": "#D0D0D0",
        "boton" : "#ABACB0",
        "fondo-xp":   "#ece9d8",
        "marcos-xp": "#7f9db9"
    }
    return colores