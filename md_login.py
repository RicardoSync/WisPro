from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkImage, CTkFrame
from PIL import Image
from tkinter import messagebox

#modulos de la aplicacion
from bk_login import login
from md_administrador import panelAdmin
from bk_recursos import colores_ui, imagenes_ui

colores = colores_ui()
iconos = imagenes_ui()

def getDatos(usuarioEntry, passwordEntry, windows):
    username = usuarioEntry.get()
    password = passwordEntry.get()
    credenciales = login(username, password)

    if credenciales:
        rol = credenciales[3]
        id_usuario = credenciales[0]

        if rol == 0:
            panelAdmin(username, id_usuario, windows)
        elif rol == 1:
            print("panel de tecnico")
        elif rol == 2:
            print("panel de cajero")
        else:
            print("No reconocemos el rol")
    
    else:
        messagebox.showerror("SpiderNet", "No podemos iniciar con esas credenciales")


def inicioSesion():
    windows = CTk()
    windows.title("Inicio de Sesion")
    windows.geometry("400x500")
    windows.resizable(False, False)
    windows._set_appearance_mode("dark")

    contenedorElementos = CTkFrame(windows, border_color=colores["marcos"], border_width=2,
                                corner_radius=10, fg_color=colores["fondo"])
    
    usuarioLabel = CTkLabel(contenedorElementos, text="Usuario", text_color="black", font=("Arial", 28, "bold"))
    usuarioEntry = CTkEntry(contenedorElementos, placeholder_text="Usuario spidernet", border_color=colores["marcos"],
                            border_width=2, corner_radius=8, width=320)
    
    passwordLabel = CTkLabel(contenedorElementos, text="Contraseña", text_color="black", font=("Arial", 28, "bold"))
    passwordEntry = CTkEntry(contenedorElementos, placeholder_text="Contraseña de usuario", border_color=colores["marcos"],
                            border_width=2, corner_radius=8, width=320, show="*")

    btnIniciar = CTkButton(contenedorElementos, border_color=colores["marcos"], border_width=2,
                        corner_radius=8, fg_color=colores["boton"], width=320,
                        text_color="black",
                        text="Iniciar Sesión",
                        command=lambda:getDatos(usuarioEntry, passwordEntry, windows))

    copyLabel = CTkLabel(contenedorElementos, text="Sotware desarrollado por Ricardo Escobedo 2025", font=("Arial", 15))

    contenedorElementos.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
    usuarioLabel.pack(padx=10, pady=10)
    usuarioEntry.pack(padx=10, pady=10)
    passwordLabel.pack(padx=10, pady=10)
    passwordEntry.pack(padx=10, pady=10)
    btnIniciar.pack(padx=10, pady=10)
    copyLabel.place(relx=0.1, rely=0.9)
    windows.mainloop()