from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame, CTk, CTkComboBox
from tkinter import messagebox

#cargamos los recursos
from bk_recursos import colores_ui, imagenes_ui
from md_creacion_usuario import creacionUusuario
iconos = imagenes_ui()
colores = colores_ui()

def enviarDatos(usuarioEntry, passwordEntry):
    usuario = usuarioEntry.get()
    password = passwordEntry.get()
    print(usuario, password)


def inicioSesion():
    windows = CTk()
    windows.title("WisPro")
    windows.geometry("1280x800")
    windows.resizable(False, False)


    #creacion de los contenedores
    contenedorImagen = CTkFrame(windows, border_color=colores["marcos"],
                            border_width=2,
                            corner_radius=0,
                            fg_color="transparent")
    
    contenedorA = CTkFrame(windows, border_color=colores["marcos"],
                            border_width=2,
                            corner_radius=0,
                            fg_color=colores["fondo"])
    

    imagen  = CTkLabel(contenedorImagen, text="", image=iconos["torre"])

    def formularioUsuario():

        contenedorFormulario = CTkFrame(contenedorA, border_width=0, corner_radius=10,
                                        fg_color="transparent",
                                        width=500,
                                        height=500
                                        )
        

        titulo = CTkLabel(contenedorFormulario, text="Inicio de Sesion", font=("Monospace", 35, "bold"),
                        text_color="white",
                        )
        

        txtB = CTkLabel(contenedorFormulario, text="Usuario", font=("Arial", 18),
                        text_color="white")
        txtC = CTkLabel(contenedorFormulario, text="Constrasena", font=("Arial", 18),
                        text_color="white")



        usuarioEntry = CTkEntry(contenedorFormulario, border_color=colores["marcos"], border_width=2,
                                corner_radius=10,
                                placeholder_text="usuario@example.com",
                                width=320)

        passwordEntry = CTkEntry(contenedorFormulario, border_color=colores["marcos"], border_width=2,
                                corner_radius=10,
                                placeholder_text="tu clave",
                                show="*",
                                width=320)

        btnCrearUsuario  = CTkButton(contenedorFormulario, text="Ingresar", border_color=colores['marcos'],
                                    border_width=2, corner_radius=10,
                                    fg_color=colores["fondo"],
                                    width=320,
                                    command=lambda: enviarDatos(usuarioEntry, passwordEntry)
                                    )
        
        btnRegistrar = CTkButton(contenedorFormulario, text="Registrar", border_color=colores["marcos"],
                                border_width=2,
                                corner_radius=10,
                                fg_color=colores["fondo"],
                                width=320,
                                command=creacionUusuario
                                )
        
        contenedorFormulario.pack(padx=10, pady=70)
        titulo.pack(padx=10, pady=20)
        txtB.pack(padx=10, pady=5)
        usuarioEntry.pack(padx=10, pady=5)
        txtC.pack(padx=10, pady=5)
        passwordEntry.pack(padx=10, pady=5)


        btnCrearUsuario.pack(padx=10, pady=40)
        btnRegistrar.pack(padx=10, pady=5)

    #posicion de los elementos
    contenedorImagen.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
    contenedorA.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)
    formularioUsuario()
    imagen.pack()

    windows.mainloop()