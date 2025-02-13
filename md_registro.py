"""
Vamos a pedir los datos al usuario que son:
    nombre, apellido, direccion, telefono, correo electronico
    creacion de su usuario y contraseña, al usuario elejido integrar el @doblenet.com
"""
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter import messagebox
from bk_recursos import colores_ui, imagenes_ui

iconos = imagenes_ui()
colores = colores_ui()


def contenedor_informacion(ventana):
    #frame de informacion
    frameInformacion = CTkFrame(ventana, border_color=colores["marcos"], border_width=2, corner_radius=6)
    icono = CTkLabel(frameInformacion, text="", image=iconos["hacker"])

    informacion = CTkLabel(frameInformacion, text_color="white", font=("Arial", 15),
                        text="Gracias por usar nuestro sistema SpiderNet enfocado en la administración\n de clientes de un Wisp/Isp\nEste software es completamente gratuito \ntanto las herramientas como el uso de alojamiento del servidor Doblenet.\nPara poder continuar por favor\n ingresa tus datos para crear una cuenta y puedas usar nuestro sistema.")

    btnInformacion = CTkButton(frameInformacion, text="Información", text_color="black",
                            border_color=colores["marcos"], border_width=2, 
                            corner_radius=6, fg_color=colores["boton"],
                            width=250)
    
    frameInformacion.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
    icono.pack(padx=10, pady=10)
    informacion.pack(padx=10, pady=10)
    btnInformacion.pack(padx=10, pady=10)

def formulario(ventana):
    #pedimos nombre, apellido, telefono, correo, usuario y contraseña

    frameFormulario = CTkFrame(ventana, border_width=2, corner_radius=6)

    nombreIspEntry = CTkEntry(frameFormulario, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        text_color="white", placeholder_text="Ingresa el nombre de tu ISP",
                        width=300)

    nombreEntry = CTkEntry(frameFormulario, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        text_color="white", placeholder_text="Ingrese su nombre (s)",
                        width=300)

    apellidoEntry = CTkEntry(frameFormulario, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        text_color="white", placeholder_text="Ingrese su apellido (s)",
                        width=300)

    
    frameFormulario.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)    
    nombreIspEntry.grid(column=0, row=0, padx=10, pady=10)
    nombreEntry.grid(column=0, row=1, padx=10, pady=10)
    apellidoEntry.grid(column=1, row=1, padx=10, pady=10)

def md_registro():
    ventana = CTk()
    ventana.title("Registro de Usuario")
    ventana.geometry("1280x800")
    ventana.resizable(False, False)
    ventana.configure(fg_color=colores["fondo"])

    contenedor_informacion(ventana)
    formulario(ventana)
    ventana.mainloop()


md_registro()