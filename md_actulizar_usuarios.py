from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkComboBox, CTkLabel
from bk_recursos import colores_ui
from bk_update import actualizarUsuario

colores = colores_ui()

def insertarElementos(nombreEntry, usuarioEntry, passwordEntry, tipoActualEntry, rol, nombre, usuario, password):
        # Insertar los valores en los campos de entrada
        rol = int(rol)
        nombreEntry.delete(0, "end")  # Limpiar antes de insertar
        usuarioEntry.delete(0, "end")
        passwordEntry.delete(0, "end")
        tipoActualEntry.delete(0, "end")  # También limpiar este campo

        nombreEntry.insert(0, nombre)
        usuarioEntry.insert(0, usuario)
        passwordEntry.insert(0, password)
        # Comprobación del rol y asignación del texto correspondiente
        if rol == 0:
            tipoActualEntry.insert(0, "Admin")
        elif rol == 1:
            tipoActualEntry.insert(0, "Tecnico")
        elif rol == 2:
            tipoActualEntry.insert(0, "Cajero")
        else:
            tipoActualEntry.insert(0, "Desconocido")  # En caso de que haya un valor inesperado

def enviarDatos(id, nombreEntry, usuarioEntry, passwordEntry, nuevoTipo, panel):
    nombre = nombreEntry.get()
    usuario = usuarioEntry.get()
    password = passwordEntry.get()
    rol = nuevoTipo.get()

    if actualizarUsuario(id, nombre, usuario, password, rol):
        panel.destroy()

def actualizarUsuariosWindows(id, nombre, usuario, password, rol):
    panel = CTkToplevel()
    panel.title(f"Actualizar Usuario {nombre}")
    panel.geometry("600x800")
    panel.resizable(False, False)
    panel._set_appearance_mode("dark")
    panel.configure(fg_color=colores["fondo"])
    tipo_usuario = ["Admin", "Tecnico", "Cajero"]



    nombreLabel = CTkLabel(panel, text="Nombre del Usuario", font=("Arial", 20, "bold"), text_color="black")
    usuarioLabel = CTkLabel(panel, text="Usuario", font=("Arial", 20, "bold"), text_color="black")
    passwordLabel = CTkLabel(panel, text="Password", font=("Arial", 20, "bold"), text_color="black")
    rolLabel = CTkLabel(panel, text="Tipo de Usuario Actual", font=("Arial", 20, "bold"), text_color="black")
    nuevoRolLabel = CTkLabel(panel, text="TIpo de Usuario Nuevo", font=("Arial", 20, "bold"), text_color="black")

    nombreEntry = CTkEntry(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320)
    usuarioEntry = CTkEntry(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320)
    passwordEntry = CTkEntry(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320)
    tipoActualEntry = CTkEntry(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320)
    nuevoTipo = CTkComboBox(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320,
                            values=tipo_usuario)
    
    btnActualizar = CTkButton(panel, text="Actualizar", border_color=colores["marcos"],
                            border_width=2, corner_radius=10, width=320,
                            fg_color=colores["boton"],
                            text_color="black",
                            command=lambda:enviarDatos(id, nombreEntry, usuarioEntry, passwordEntry, nuevoTipo, panel))
    
    btnCanelar = CTkButton(panel, text="Cancelar", border_color=colores["marcos"],
                            border_width=2, corner_radius=10, width=320,
                            command=panel.destroy,
                            fg_color=colores["boton"],
                            text_color="black")



    nombreLabel.pack(padx=10, pady=10)
    nombreEntry.pack(padx=10, pady=10)
    usuarioLabel.pack(padx=10, pady=10)
    usuarioEntry.pack(padx=10, pady=10)
    passwordLabel.pack(padx=10, pady=10)
    passwordEntry.pack(padx=10, pady=10)
    rolLabel.pack(padx=10, pady=10)
    tipoActualEntry.pack(padx=10, pady=10)
    nuevoRolLabel.pack(padx=10, pady=10)
    nuevoTipo.pack(padx=10, pady=10)
    btnActualizar.pack(padx=10, pady=10)
    btnCanelar.pack(padx=10, pady=10)
    insertarElementos(nombreEntry, usuarioEntry, passwordEntry, tipoActualEntry, rol, nombre,
                    usuario, password)
    panel.mainloop()