from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkImage
from PIL import Image
from tkinter import messagebox

#modulos de la aplicacion
from bk_login import login
from md_administrador import panelAdmin

def cargarImagenes():
    imagenes = {
        "logo": CTkImage(light_image=Image.open("img/logo.png"),
                        dark_image=Image.open("img/logo.png"),
                        size=(200,200))
    }
    return imagenes

def getDatos(usuarioEntry, passwordEntry, windows):
    username = usuarioEntry.get()
    password = passwordEntry.get()
    credenciales = login(username, password)

    if credenciales:
        rol = credenciales[2]

        if rol == 0:
            panelAdmin(username, rol, windows)
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
    windows.geometry("600x800")
    windows.resizable(False, False)
    windows._set_appearance_mode("dark")
    icono = cargarImagenes()

    #cargamos la imagen
    logo = CTkLabel(windows, text="", image=icono["logo"])
    welcome = CTkLabel(windows, text="Bienvenido a SpiderNet", font=("Monospace", 25, "bold"),
                    text_color="white")
    

    usurioLabel = CTkLabel(windows, text="Username", font=("Arial", 18),
                        text_color="white")
    
    passwordLabel = CTkLabel(windows, text="Pssword", font=("Arial", 18),
                        text_color="white")
    
    usuarioEntry = CTkEntry(windows, border_width=2, corner_radius=10,
                            placeholder_text="username", width=320)
    
    passwordEntry = CTkEntry(windows, border_width=2, corner_radius=10,
                            placeholder_text="password", width=320,
                            show="*")
    
    btnIniciar = CTkButton(windows, text="Iniciar", border_width=2, corner_radius=10,
                        width=320,
                        command=lambda:getDatos(usuarioEntry, passwordEntry, windows))
    
    btnCancelar = CTkButton(windows, text="Cancelar", border_width=2, corner_radius=10,
                            width=320,
                            command=windows.destroy)
    
    logo.pack(padx=10, pady=10)
    welcome.pack(padx=10, pady=10)
    usurioLabel.pack(padx=10, pady=10)
    usuarioEntry.pack(padx=10, pady=10)
    passwordLabel.pack(padx=10, pady=10)
    passwordEntry.pack(padx=10, pady=10)
    btnIniciar.pack(padx=10, pady=10)
    btnCancelar.pack(padx=10, pady=10)

    windows.mainloop()