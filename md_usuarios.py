from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkComboBox
from tkinter import messagebox, ttk, END

#modulos
from bk_recursos import colores_ui
from bk_consultas import consultaUsuarios

colores = colores_ui()

def formularioUI(formBanner, windows):
    tipo_usuario = ["Admin", "Tecnico", "Cajero"]

    nombreLabel = CTkLabel(formBanner, text="Nombre Completo", font=("Arial", 18, "bold"), text_color="black")

    nombreEntry = CTkEntry(formBanner, placeholder_text="Ricardo Escobedo", border_width=2,
                        border_color=colores["marcos"], corner_radius=10,
                        width=200)
    
    usernameLabel = CTkLabel(formBanner, text="Nombre de usuario", font=("Arial", 18, "bold"), text_color="black")

    usernameEntry = CTkEntry(formBanner, placeholder_text="ricardo@doblenet.com", border_width=2,
                        border_color=colores["marcos"], corner_radius=10,
                        width=200)
    
    passwordLabel = CTkLabel(formBanner, text="Contrasenia", font=("Arial", 18, "bold"), text_color="black")

    passwordEntry = CTkEntry(formBanner, border_width=2,
                        border_color=colores["marcos"], corner_radius=10,
                        show="*",
                        width=200)

    tpUusuario = CTkLabel(formBanner, text="Tipo de usuario", font=("Arial", 18, "bold"), text_color="black")

    
    tipoUsuario = CTkComboBox(formBanner, values=tipo_usuario, border_color=colores["marcos"], 
                            border_width=2, corner_radius=10,
                            width=200)
    
    btnRegistrar  = CTkButton(formBanner, text="Registrar", border_width=2, border_color=colores["marcos"],
                            corner_radius=10, fg_color=colores["boton"],
                            width=200,
                            text_color="black")

    btnCancelar  = CTkButton(formBanner, text="Cancelar", border_width=2, border_color=colores["marcos"],
                            corner_radius=10, fg_color=colores["boton"],
                            width=200,
                            text_color="black",
                            command=windows.destroy)

    nombreLabel.pack(padx=10, pady=10)
    nombreEntry.pack(padx=10, pady=10)
    usernameLabel.pack(padx=10, pady=10)
    usernameEntry.pack(padx=10, pady=10)
    passwordLabel.pack(padx=10, pady=10)
    passwordEntry.pack(padx=10, pady=10)
    tpUusuario.pack(padx=10, pady=10)
    tipoUsuario.pack(padx=10, pady=10)
    btnRegistrar.pack(padx=10, pady=10)
    btnCancelar.pack(padx=10, pady=10)


def tablaUsuarios(windows):
    usuarios = consultaUsuarios()

    contenedorTabla = CTkFrame(windows, border_width=2, border_color=colores["marcos"],
                        corner_radius=0, fg_color=colores["fondo"])
    

    tabla = ttk.Treeview(contenedorTabla, columns=("Nombre", "Username", "Password", "Rol"), show="headings")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Username", text="Username")
    tabla.heading("Password", text="Password")
    tabla.heading("Rol", text="Rol")

    for item in tabla.get_children():
        tabla.delete(item)

    for usuario in usuarios:
        tabla.insert("", END, values=usuario)

    contenedorTabla.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tabla.pack(expand=True, fill="both")

def creacionUsuarios():
    windows = CTkToplevel()
    windows.title("Nuevo Usuario")
    windows.geometry("1280x800")
    windows.resizable(False, False)
    windows._set_appearance_mode("dark")


    #creamos el banner de formulario
    formBanner = CTkFrame(windows, border_width=2, border_color=colores["marcos"],
                        corner_radius=0, fg_color=colores["fondo"])
    

    
    #posicion de elementos
    formBanner.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)

    formularioUI(formBanner,windows)
    tablaUsuarios(windows)
    windows.mainloop()