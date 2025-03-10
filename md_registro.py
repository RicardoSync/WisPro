from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from bk_recursos import colores_ui, imagenes_ui
from tkinter import messagebox
from bk_creacion_cuenta import enviar_datos
import random
import string
import webbrowser
import json
from md_tengo_cuenta import md_cuenta_existente
iconos = imagenes_ui()
colores = colores_ui()


def obtener_datos(usernameEntry, passwordEntry, nombreISPEntry, nombreEntry, telefonoEntry, emailEntry, direccionEntry, btnINicio):
    username = usernameEntry.get()
    password = passwordEntry.get()
    nombreISP = nombreISPEntry.get()
    nombre = nombreEntry.get()
    telefono = telefonoEntry.get()
    email = emailEntry.get()
    direccion = direccionEntry.get()

    if not username or not password or not nombreISP or not nombre or not telefono or not email or not direccion:
        messagebox.showerror("SpiderNet", "Todos los campos son obligatorios")
        return

    # Generar una cadena con 5 letras aleatorias
    letras_aleatorias = ''.join(random.choices(string.ascii_lowercase, k=15))
    # Crear un nombre de base de datos utilizando los valores dados y las letras aleatorias
    nombre_bd = f"{nombreISP}_{nombre}_{email.split('@')[0]}_{direccion[:5]}_{letras_aleatorias}"

    # Limitar a un tamaño máximo de caracteres si es necesario (por ejemplo, 64 caracteres)
    nombre_db = nombre_bd[:64]

    if enviar_datos(username, password, nombreISP, nombre, telefono, email, direccion, nombre_db):
        # Datos base para la configuración
        config = {
            "host": "servidores_escobedo",
            "port": 3389,
            "user": "usuario_escobedo",
            "password": "password_escobed",
            "database": nombre_bd
        }

        # Guardar en un archivo JSON
        with open("config.json", "w") as file:
            json.dump(config, file, indent=4)

    btnINicio.grid(column=0, row=4, padx=10, pady=10)


def contenedor_imagen(windows):
    frameImagen = CTkFrame(windows, border_width=2, corner_radius=6, fg_color="#2b2b2b")
    
    logo = CTkLabel(frameImagen, text="", image=iconos["hacker"])
    info_label = CTkLabel(
        frameImagen,
        text=(
            "Este software es gratuito. "
            "El único costo es el alojamiento de los datos en nuestros servidores.\n"
            "Puede optar por una base de datos local o en su propio servidor.\n"
            "Para más información, contáctenos."
        ),
        justify="center",
        wraplength=250,
        font=("Arial", 15),
        text_color="white"
    )
    
    frameImagen.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
    logo.pack(padx=10, pady=10)
    info_label.pack(padx=10, pady=10)

def inicioSesion(windows):
    from md_login_cuenta import inicioSesion
    inicioSesion(windows)

def formulario_cliente(windows):
    #frame con las opciones
    frameFormulario = CTkFrame(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color="#2b2b2b")

    frameCuenta = CTkFrame(windows, border_width=2, corner_radius=6, border_color=colores["marcos"],
                        fg_color="#2b2b2b")

    usernameLabel = CTkLabel(frameCuenta, text="Nombre de usuario", text_color="white", font=("Arial", 15, "bold"))
    usernameEntry = CTkEntry(frameCuenta, placeholder_text="usuariochido", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="black", width=300)
    
    passwordLabel = CTkLabel(frameCuenta, text="Contraseña de usuario", text_color="white", font=("Arial", 15, "bold"))
    passwordEntry = CTkEntry(frameCuenta, placeholder_text="dificil789", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="black", width=300)
    
    #nombre ISP, nombre, telefono, email, direccion 
    nombreLabel = CTkLabel(frameFormulario, text="Nombre de ISP (Sin Espacios)", text_color="white", font=("Arial", 15, "bold"))
    nombreISPEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo DOBLENET", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="black", width=300)
    
    nombrePersona = CTkLabel(frameFormulario, text="Su nombre (Sin apellidos ni Espacios)", text_color="white", font=("Arial", 15, "bold"))
    nombreEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo Ricardo Escobedo", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="black", width=300)
    
    telefonoLabel = CTkLabel(frameFormulario, text="Telefono celular", text_color="white", font=("Arial", 15, "bold"))
    telefonoEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo +5214981442266", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="black", width=300)
    
    emailLabel = CTkLabel(frameFormulario, text="Correo electronico", text_color="white", font=("Arial", 15, "bold"))
    emailEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo usuario@example.com", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="black", width=300)
    
    direccionLabel = CTkLabel(frameFormulario, text="Munipio / Localidad", text_color="white", font=("Arial", 15, "bold"))
    direccionEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo Loreto", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="black", width=300)

    btnCrearCuenta = CTkButton(frameCuenta, text="Crear Cuenta",
                        text_color="black", border_color=colores["marcos"],
                        border_width=2, corner_radius=6,
                        fg_color=colores["boton"], width=300,
                        command=lambda:obtener_datos(usernameEntry, passwordEntry, nombreISPEntry, nombreEntry, telefonoEntry, emailEntry, direccionEntry,
                                                    btnINicio))

    btnIniciarSesion = CTkButton(frameCuenta, text="Ya tengo cuenta!",
                        text_color="black", border_color=colores["marcos"],
                        border_width=2, corner_radius=6,
                        fg_color=colores["boton"], width=300,
                        command=lambda:md_cuenta_existente(windows))
    
    btnINicio = CTkButton(frameCuenta, text="Inicias Sesion", font=("Arial", 15, "bold"),
                        text_color="white", border_color=colores["marcos"],
                        border_width=2, corner_radius=6,
                        fg_color="green", width=300,
                        command=lambda:inicioSesion(windows))
    
    btnProyecto = CTkButton(frameCuenta, text="Proyecto GitHub",
                        text_color="black", border_color=colores["marcos"],
                        border_width=2, fg_color=colores["boton"],
                        width=300, command=lambda:webbrowser.open("https://github.com/RicardoSync/WisPro.git"))
    
    btnContacto = CTkButton(frameCuenta, text="Contactamé",
                        text_color="black", border_color=colores["marcos"],
                        border_width=2, fg_color=colores["boton"],
                        width=300, command=lambda:webbrowser.open("https://www.facebook.com/profile.php?id=100065750894627"))

    frameFormulario.place(relx=0.5, rely=0.0, relheight=0.5, relwidth=0.5)
    nombreLabel.grid(column=0, row=0, padx=10, pady=10)
    nombrePersona.grid(column=1, row=0, padx=10, pady=10)
    nombreISPEntry.grid(column=0, row=1, padx=10, pady=10)
    nombreEntry.grid(column=1, row=1, padx=10, pady=10)

    telefonoLabel.grid(column=0, row=2, padx=10, pady=10)
    emailLabel.grid(column=1, row=2, padx=10, pady=10)
    telefonoEntry.grid(column=0, row=3, padx=10, pady=10)
    emailEntry.grid(column=1, row=3, padx=10, pady=10)

    direccionLabel.grid(column=0, row=4, padx=10, pady=10)
    direccionEntry.grid(column=0, row=5, padx=10, pady=10)

    frameCuenta.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
    usernameLabel.grid(column=0, row=0, padx=10, pady=10)
    passwordLabel.grid(column=1, row=0, padx=10, pady=10)
    usernameEntry.grid(column=0, row=1, padx=10, pady=10)
    passwordEntry.grid(column=1, row=1, padx=10, pady=10)
    btnCrearCuenta.grid(column=0, row=2, padx=10, pady=10)
    btnIniciarSesion.grid(column=1, row=2, padx=10, pady=10)
    btnProyecto.grid(column=0, row=3, padx=10, pady=10)
    btnContacto.grid(column=1, row=3, padx=10, pady=10)

def md_registro_windows():
    windows = CTk()
    windows.title("Creación de Cuenta")
    windows.geometry("1280x600")
    windows.resizable(False, False)

    formulario_cliente(windows)
    contenedor_imagen(windows)
    windows.mainloop()
