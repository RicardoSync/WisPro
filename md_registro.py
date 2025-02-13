from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton
from bk_recursos import colores_ui, imagenes_ui

iconos = imagenes_ui()
colores = colores_ui()


def formulario_cliente(windows):
    #frame con las opciones
    frameFormulario = CTkFrame(windows, border_color=colores["marcos"], border_width=2, corner_radius=6)

    frameCuenta = CTkFrame(windows, border_width=2, corner_radius=6, border_color=colores["marcos"])



    usernameLabel = CTkLabel(frameCuenta, text="Nombre de usuario", text_color="white", font=("Arial", 15, "bold"))
    usernameEntry = CTkEntry(frameCuenta, placeholder_text="usuariochido", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, text_color="white", width=300)
    
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