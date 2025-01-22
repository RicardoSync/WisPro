from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame, CTkToplevel, CTkComboBox
from tkinter import messagebox

#cargamos los recursos
from bk_recursos import colores_ui, imagenes_ui
from bk_creacion_usuario import insertarUsuario

iconos = imagenes_ui()
colores = colores_ui()


def creacionUusuario():
    windows = CTkToplevel()
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


        def enviarDatos():
            nombre = nombreEntry.get()
            usuario = usuarioEntry.get()
            password = passwordEntry.get()
            tipo_usuario = tipoUsuario.get()

            if len(nombre)>0:
                if insertarUsuario(nombre, usuario, password, tipo_usuario):
                    windows.destroy()
            else:
                messagebox.showerror("WisPro", "No podemos registrar un usuario sin nombre")
    

        roles = ["admin", "tecnico", "cajero"]

        contenedorFormulario = CTkFrame(contenedorA, border_width=0, corner_radius=10,
                                        fg_color="transparent",
                                        width=500,
                                        height=500
                                        )
        

        titulo = CTkLabel(contenedorFormulario, text="Creacion de Usuario", font=("Monospace", 35, "bold"),
                        text_color="white",
                        )
        
        txtA = CTkLabel(contenedorFormulario, text="Nombre Completo", font=("Arial", 18),
                        text_color="white")
        txtB = CTkLabel(contenedorFormulario, text="Usuario", font=("Arial", 18),
                        text_color="white")
        txtC = CTkLabel(contenedorFormulario, text="Constrasena", font=("Arial", 18),
                        text_color="white")
        txtD = CTkLabel(contenedorFormulario, text="Rol Asignado", font=("Arial", 18),
                        text_color="white")

        nombreEntry = CTkEntry(contenedorFormulario, border_color=colores["marcos"], border_width=2,
                                corner_radius=10, 
                                placeholder_text="Ricardo Escobedo",
                                width=320)
        
        usuarioEntry = CTkEntry(contenedorFormulario, border_color=colores["marcos"], border_width=2,
                                corner_radius=10,
                                placeholder_text="usuario@example.com",
                                width=320)

        passwordEntry = CTkEntry(contenedorFormulario, border_color=colores["marcos"], border_width=2,
                                corner_radius=10,
                                placeholder_text="tu clave",
                                show="*",
                                width=320)
        
        tipoUsuario = CTkComboBox(contenedorFormulario, border_color=colores["marcos"], border_width=2,
                                corner_radius=10,
                                values=roles,
                                width=320)
        
        btnCrearUsuario  = CTkButton(contenedorFormulario, text="Registrar Usuario", border_color=colores['marcos'],
                                    border_width=2, corner_radius=10,
                                    fg_color=colores["fondo"],
                                    width=320,
                                    command=enviarDatos
                                    )
        
        btnCancelar = CTkButton(contenedorFormulario, text="Cancelar", border_color=colores["marcos"],
                                border_width=2,
                                corner_radius=10,
                                fg_color=colores["fondo"],
                                width=320,
                                command=windows.destroy
                                )
        
        contenedorFormulario.pack(padx=10, pady=70)
        titulo.pack(padx=10, pady=20)
        txtA.pack(padx=10, pady=5)
        nombreEntry.pack(padx=10, pady=5)
        txtB.pack(padx=10, pady=5)
        usuarioEntry.pack(padx=10, pady=5)
        txtC.pack(padx=10, pady=5)
        passwordEntry.pack(padx=10, pady=5)
        txtD.pack(padx=10, pady=5)
        tipoUsuario.pack(padx=10, pady=5)

        btnCrearUsuario.pack(padx=10, pady=40)
        btnCancelar.pack(padx=10, pady=5)

    #posicion de los elementos
    contenedorImagen.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)
    contenedorA.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)
    formularioUsuario()
    imagen.pack()

    windows.mainloop()