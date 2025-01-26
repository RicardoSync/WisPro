from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkComboBox
from tkinter import messagebox, ttk, END
import tkinter as tk

#modulos
from bk_recursos import colores_ui
from bk_consultas import consultaUsuarios
from bk_insert import insertarUsuarios
from bk_delete import eliminarUsuario
from md_actulizar_usuarios import actualizarUsuariosWindows

colores = colores_ui()

def enviarEliminacion(tabla, windows):
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showerror("SpiderNet", "Selecciona un usuario para poder eliminarlo")
    
    identificador = tabla.item(seleccionado, "values")

    confirmacion = messagebox.askyesno("SpiderNet", "Seguro que desea eliminar al usuario?")

    if confirmacion:
        id = identificador[0]
        eliminarUsuario(id)
        tablaUsuarios(windows)
    else:
        messagebox.showinfo("SpiderNet", "No se elimino ningun elemento")

def enviarActializacion(tabla, windows):
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showinfo("SpiderNet", "No podemos actualizar sin ningun dato")
    
    identificador = tabla.item(seleccionado, "values")
    id = identificador[0]
    nombre = identificador[1]
    usuario = identificador[2]
    password = identificador[3]
    rol = identificador[4]
    actualizarUsuariosWindows(id, nombre, usuario, password, rol)


def getDatos(nombreEntry, usernameEntry, passwordEntry, tipoUsuario, windows):
    nombre = nombreEntry.get()
    username = usernameEntry.get()
    password = passwordEntry.get()
    rol = tipoUsuario.get()

    if not nombre or not username or not password or not rol:
        messagebox.showerror("SpiderNet", "Todos los campos son obligatorios")
        return

    insertarUsuarios(nombre, username, password, rol)
    #messagebox.showinfo("SpiderNet", "Usuario registrado exitosamente")
    tablaUsuarios(windows)

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
                            text_color="black",
                            command=lambda:getDatos(nombreEntry, usernameEntry, passwordEntry, tipoUsuario, windows)
                            )

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

    contenedorTabla = CTkFrame(windows, border_width=2, border_color=colores["marcos"],
                        corner_radius=0, fg_color=colores["fondo"])
    

    tabla = ttk.Treeview(contenedorTabla, columns=("ID", "Nombre", "Username", "Password", "Rol"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Username", text="Username")
    tabla.heading("Password", text="Password")
    tabla.heading("Rol", text="Rol")

    usuarios = consultaUsuarios()

    for item in tabla.get_children():
        tabla.delete(item)

    for usuario in usuarios:
        tabla.insert("", END, values=usuario)

    contenedorTabla.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tabla.pack(expand=True, fill="both")

    #creacion del menu contextual
    menu = tk.Menu(tabla, tearoff=0)
    menu.add_command(label="Editar", command=lambda:enviarActializacion(tabla, windows))
    menu.add_command(label="Eliminar", command=lambda:enviarEliminacion(tabla, windows))
    menu.add_command(label="Actualizar", command=lambda:tablaUsuarios(windows))

    def mostrar_menu(event):
        seleccion = tabla.selection()
        if seleccion:  # Solo mostrar menú si hay un ítem seleccionado
            menu.post(event.x_root, event.y_root)

    tabla.bind("<Button-3>", mostrar_menu)  # Evento clic derecho

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