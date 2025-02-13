from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from bk_recursos import colores_ui, imagenes_ui

iconos = imagenes_ui()
colores = colores_ui()


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
    
    nombrePersona = CTkLabel(frameFormulario, text="Su nombre", text_color="white", font=("Arial", 15, "bold"))
    nombreEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo Ricardo Escobedo", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="white", width=300)
    
    telefonoLabel = CTkLabel(frameFormulario, text="Telefono celular", text_color="white", font=("Arial", 15, "bold"))
    telefonoEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo +5214981442266", border_color=colores["marcos"], border_width=2,
                            corner_radius=6, text_color="white", width=300)
    
    emailLabel = CTkLabel(frameFormulario, text="Correo electronico", text_color="white", font=("Arial", 15, "bold"))
    emailEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo usuario@example.com", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="white", width=300)
    
    direccionLabel = CTkLabel(frameFormulario, text="Dirección", text_color="white", font=("Arial", 15, "bold"))
    direccionEntry = CTkEntry(frameFormulario, placeholder_text="Ejemplo Calle Falsa #12", border_color=colores["marcos"], border_width=2,
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
                        fg_color=colores["boton"], width=300)

    btnIniciarSesion = CTkButton(frameCuenta, text="Iniciar Sesión",
                        text_color="black", border_color=colores["marcos"],
                        border_width=2, corner_radius=6,
                        fg_color=colores["boton"], width=300)

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

def md_registro_windows():
    windows = CTk()
    windows.title("Creación de Cuenta")
    windows.geometry("1280x600")
    windows.resizable(False, False)

    formulario_cliente(windows)
    windows.mainloop()



md_registro_windows()