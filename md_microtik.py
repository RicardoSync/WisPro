from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkFrame, CTkLabel
from tkinter import ttk, END, Menu, messagebox
from bk_recursos import colores_ui, imagenes_ui
from md_microtik_credenciales import panelMicrotik
from bk_consultas import consultar_microtiks
from bk_delete import eliminar_microtik
from bk_update import actualizar_microtik

colores = colores_ui()
iconos = imagenes_ui()

def enviar_datos(id, username, passwordEntry, ipEntry, nombreEntry):
    username = username.get()
    password = passwordEntry.get()
    ip = ipEntry.get()
    nombre = nombreEntry.get()

    if not username or not password or not ip or not nombre:
        messagebox.showwarning('SpiderNet', "Todos los campos son necesarios")
        return
    if actualizar_microtik(id, username, password, ip, nombre):
        messagebox.showinfo("SpiderNet", "El equipo fue actualizado")
    else:
        messagebox.showerror("SpiderNet", "No logramos actualizar el equipo")

def editar_windows(id, nombre, user, password, ip):
    windows = CTkToplevel()
    windows.title(f"Actualizar equipo {nombre}")
    windows.geometry("800x250")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    frameOpciones = CTkFrame(windows, border_color=colores["marcos"], border_width=2,
                            corner_radius=0, fg_color=colores["fondo"]
                            )
    
    logo = CTkLabel(frameOpciones, text="", image=iconos["equipo"])


    contenedor = CTkFrame(windows, border_color=colores['marcos'], border_width=2,
                        corner_radius=8, fg_color=colores["fondo"])
    
    userName = CTkLabel(contenedor, text="Usuario", font=("Arial", 20), text_color="white")
    username = CTkEntry(contenedor, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        placeholder_text="admin", text_color="white", width=250)
    
    passwordLabel = CTkLabel(contenedor, text="Contraseña", font=("Arial", 20), text_color="white")
    passwordEntry = CTkEntry(contenedor, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        placeholder_text="admin", text_color="white", width=250, show="*")

    ipLabel = CTkLabel(contenedor, text="Ip Microtik", font=("Arial", 20), text_color="white")
    ipEntry = CTkEntry(contenedor, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        placeholder_text="192.168.1.254", text_color="white", width=250)
    
    nombreLabel = CTkLabel(contenedor, text="Nombre Microtik", font=("Arial", 20), text_color="white")
    nombreEntry = CTkEntry(contenedor, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        placeholder_text="Microtik clientes Zona A", text_color="white", width=250)


    btnGuardar = CTkButton(contenedor, border_color=colores["marcos"],
                        border_width=2, corner_radius=6, fg_color=colores["boton"],
                        text="Actualizar", text_color="black", width=250,
                        command=lambda:enviar_datos(id, username, passwordEntry, ipEntry, nombreEntry))
    

    contenedor.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    userName.grid(column=0, row=0, padx=10, pady=10)
    passwordLabel.grid(column=1, row=0, padx=10, pady=10)


    username.grid(column=0, row=1, padx=10, pady=10)
    passwordEntry.grid(column=1, row=1, padx=10, pady=10)
    ipLabel.grid(column=0, row=2, padx=10, pady=10)
    nombreLabel.grid(column=1, row=2, padx=10, pady=10)
    ipEntry.grid(column=0, row=3, padx=10, pady=10)
    nombreEntry.grid(column=1, row=3, padx=10, pady=10)
    btnGuardar.grid(column=0, row=4, padx=10, pady=10)
    frameOpciones.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    logo.pack(padx=10, pady=10)

    username.insert(0, user)
    passwordEntry.insert(0, password)
    ipEntry.insert(0, ip)
    nombreEntry.insert(0, nombre)
    windows.mainloop()

def editar_equipo(contenedorTable):
    selection = contenedorTable.selection()
    if not selection:
        messagebox.showwarning("SpiderNet", "No podemos editar si no seleccionas un equipo")
        return
    
    identificador = contenedorTable.item(selection, "values")
    id = identificador[0]
    nombre = identificador[1]
    user = identificador[2]
    ip = identificador[3]
    password = identificador[4]
    editar_windows(id, nombre, user, password, ip)

def insertar_elementos(contenedorTable):
    lista_microtiks = consultar_microtiks()

    for item in contenedorTable.get_children():
        contenedorTable.delete(item)
    
    for microtik in lista_microtiks:
        contenedorTable.insert("", END, values=microtik)

def eliminar(contenedorTable):
    selection = contenedorTable.selection()

    if not selection:
        messagebox.showwarning("SpiderNet", "Anteas de eliminar por favor selecciona un elemento")
        return
    
    identificador = contenedorTable.item(selection, "values")
    if eliminar_microtik(id=identificador[0]):
        messagebox.showinfo("SpiderNet", "Equipo eliminado de la base de datos")
        insertar_elementos(contenedorTable)
    else:
        messagebox.showerror("SpiderNet", "Ocurrio un error al intentar eliminar")

def tabla(windows):
    frameTabla = CTkFrame(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["fondo"])
    
    contenedorTable = ttk.Treeview(frameTabla, columns=("ID", "Nombre", "Username", "Ip", "Contraseña"), show="headings")
    contenedorTable.heading("ID", text="ID")
    contenedorTable.heading("Nombre", text="Nombre")
    contenedorTable.heading("Username", text="Username")
    contenedorTable.heading("Ip", text="Ip")
    contenedorTable.heading("Contraseña", text="Contraseña")

    frameTabla.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
    contenedorTable.pack(expand=True, fill="both")

    insertar_elementos(contenedorTable)

    #creacion del menu contextual
    menu = Menu(contenedorTable, tearoff=0)
    menu.add_command(label="Editar", command=lambda:editar_equipo(contenedorTable))
    menu.add_command(label="Eliminar", command=lambda:eliminar(contenedorTable))
    menu.add_command(label="Agregar", command=panelMicrotik)
    menu.add_command(label="Actualizar", command=lambda:insertar_elementos(contenedorTable))

    def mostrar_menu(event):
        seleccion = contenedorTable.selection()
        menu.post(event.x_root, event.y_root)

    contenedorTable.bind("<Button-3>", mostrar_menu)  # Evento clic derecho


def modulo_microtik():
    windows = CTkToplevel()
    windows.title("Microtiks")
    windows.geometry("1000x700")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    #barra superior 
    barraSuperior = CTkFrame(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color=colores["fondo"])
    
    nombreEntry = CTkEntry(barraSuperior, placeholder_text="Ip del microtik", border_color=colores["marcos"],
                        border_width=2, corner_radius=6, text_color="black", width=320)
    
    btnBuscar = CTkButton(barraSuperior, text="Buscar", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, fg_color=colores["boton"], text_color="black", width=320)
    

    barraSuperior.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    nombreEntry.grid(column=0, row=0, padx=10, pady=20)
    btnBuscar.grid(column=1, row=0, padx=10, pady=20)
    tabla(windows)
    windows.mainloop()
