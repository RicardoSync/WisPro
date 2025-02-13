from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from bk_recursos import colores_ui, imagenes_ui
from tkinter import messagebox
from bk_creacion_cuenta import enviar_datos
import random
import string
import webbrowser
import json
iconos = imagenes_ui()
colores = colores_ui()


def obtener_datos(usernameEntry, passwordEntry, nombreISPEntry, nombreEntry, telefonoEntry, emailEntry, direccionEntry):
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
    letras_aleatorias = ''.join(random.choices(string.ascii_lowercase, k=5))
    # Crear un nombre de base de datos utilizando los valores dados y las letras aleatorias
    nombre_bd = f"{nombreISP}_{nombre}_{email.split('@')[0]}_{telefono}_{direccion[:5]}_{letras_aleatorias}"

    # Limitar a un tamaño máximo de caracteres si es necesario (por ejemplo, 64 caracteres)
    nombre_db = nombre_bd[:64]

    if enviar_datos(username, password, nombreISP, nombre, telefono, email, direccion, nombre_db):
        # Datos base para la configuración
        config = {
            "host": "200.234.227.222",
            "port": 3389,
            "user": "cisco",
            "password": "MinuzaFea265/",
            "database": nombre_db
        }

        # Guardar en un archivo JSON
        with open("config.json", "w") as file:
            json.dump(config, file, indent=4)

def iniciar_sesion(windows):
    from md_login import inicioSesion
    windows.destroy()
    inicioSesion()


def contenedor_imagen(windows):
    frameImagen = CTkFrame(windows, border_width=2, corner_radius=6)
    
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
        font=("Arial", 15)
    )
    
    frameImagen.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
    logo.pack(padx=10, pady=10)
    info_label.pack(padx=10, pady=10)

def formulario_cliente(windows):
    #frame con las opciones
    frameFormulario = CTkFrame(windows, border_color=colores["marcos"], border_width=2, corner_radius=6)

<<<<<<< Updated upstream
    frameCuenta = CTkFrame(windows, border_width=2, corner_radius=6, border_color=colores["marcos"])
=======
    informacion = CTkLabel(
        frameInformacion,
        text=(
            "Gracias por usar nuestro sistema SpiderNet, enfocado en la administración "
            "de clientes de un WISP/ISP.\n\n"
            "Este software es completamente gratuito, incluyendo tanto las herramientas "
            "como el uso de alojamiento del servidor DOBLENET.\n\n"
            "Para continuar, por favor ingresa tus datos para crear una cuenta "
            "y comenzar a usar nuestro sistema."
        ),
        text_color="white",
        font=("Arial", 15),
        wraplength=400,  # Ajusta según el tamaño de tu frame
        justify="center"  # Centra el texto
    )
>>>>>>> Stashed changes

    usernameLabel = CTkLabel(frameCuenta, text="Nombre de usuario", text_color="white", font=("Arial", 15, "bold"))
    usernameEntry = CTkEntry(frameCuenta, placeholder_text="usuariochido", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="white", width=300)
    
<<<<<<< Updated upstream
    passwordLabel = CTkLabel(frameCuenta, text="Contraseña de usuario", text_color="white", font=("Arial", 15, "bold"))
    passwordEntry = CTkEntry(frameCuenta, placeholder_text="dificil789", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="white", width=300)
    
    #nombre ISP, nombre, telefono, email, direccion 
    nombreLabel = CTkLabel(frameFormulario, text="Nombre de ISP", text_color="white", font=("Arial", 15, "bold"))
    nombreISPEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo DOBLENET", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="white", width=300)
    
    nombrePersona = CTkLabel(frameFormulario, text="Su nombre (Sin apellidos ni Espacios)", text_color="white", font=("Arial", 15, "bold"))
    nombreEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo Ricardo Escobedo", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="white", width=300)
    
    telefonoLabel = CTkLabel(frameFormulario, text="Telefono celular", text_color="white", font=("Arial", 15, "bold"))
    telefonoEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo +5214981442266", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="white", width=300)
    
    emailLabel = CTkLabel(frameFormulario, text="Correo electronico", text_color="white", font=("Arial", 15, "bold"))
    emailEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo usuario@example.com", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="white", width=300)
    
    direccionLabel = CTkLabel(frameFormulario, text="Munipio / Localidad", text_color="white", font=("Arial", 15, "bold"))
    direccionEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo Loreto", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="white", width=300)
=======
    frameInformacion.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
    icono.pack(padx=10, pady=10)
    informacion.pack(padx=10, pady=10)
    btnInformacion.pack(padx=10, pady=10)

def formulario(ventana):
    #pedimos nombre, apellido, telefono, correo, usuario y contraseña

    frameFormulario = CTkFrame(ventana, border_width=2, corner_radius=6)

    nombreIspLabel = CTkLabel(frameFormulario, text="Nombre de ISP/Wisp", text_color="white", font=("Arial", 20))
    nombreIspEntry = CTkEntry(frameFormulario, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            text_color="white", placeholder_text="Ej DOBLENET",
                            width=250)
    
    nombreLabel = CTkLabel(frameFormulario, text="Ingrese su nombre", text_color="white", font=("Arial", 20))
    telefonoLabel = CTkLabel(frameFormulario, text="Telefono celular", text_color="white", font=("Arial", 20))
    correoLabel = CTkLabel(frameFormulario, text="Correo electronico", text_color="white", font=("Arial", 20))
    direccionLabel = CTkLabel(frameFormulario, text="Direccion de ISP", text_color="white", font=("Arial", 20))

    frameFormulario.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)    
    nombreIspLabel.grid(column=0, row=0, padx=10, pady=10)
    nombreIspEntry.grid(column=0, row=1, padx=10, pady=10)

    nombreLabel.grid(column=1, row=0, padx=10, pady=10)

>>>>>>> Stashed changes

    btnCrearCuenta = CTkButton(frameCuenta, text="Crear Cuenta",
                        text_color="black", border_color=colores["marcos"],
                        border_width=2, corner_radius=6,
                        fg_color=colores["boton"], width=300,
                        command=lambda:obtener_datos(usernameEntry, passwordEntry, nombreISPEntry, nombreEntry, telefonoEntry, emailEntry, direccionEntry))

    btnIniciarSesion = CTkButton(frameCuenta, text="Iniciar Sesión",
                        text_color="black", border_color=colores["marcos"],
                        border_width=2, corner_radius=6,
                        fg_color=colores["boton"], width=300,
                        command=lambda:iniciar_sesion(windows))
    
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
