from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton, CTkFrame
from bk_recursos import colores_ui, imagenes_ui
from bk_insert import insertar_microtik
from tkinter import messagebox

iconos = imagenes_ui()
colores = colores_ui()

def enviar_datos(username, passwordEntry, ipEntry, nombreEntry, windows):
    username = username.get()
    password = passwordEntry.get()
    ip = ipEntry.get()
    nombre = nombreEntry.get()

    if not username or not password or not ip or not nombre:
        messagebox.showwarning("SpiderNet", "Todos los campos son oblitatorios")
        return
    
    if insertar_microtik(nombre, username, password, ip):
        windows.destroy()
    else:
        messagebox.showerror("SpiderNet", "No logramos almacenar el equipo")

def formulario(windows):
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
                        text="Guardar", text_color="black", width=250,
                        command=lambda:enviar_datos(username, passwordEntry, ipEntry, nombreEntry, windows))
    


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

def panelMicrotik():
    windows = CTkToplevel()
    windows.title("Credenciales de Microtik")
    windows.geometry("800x250")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    frameOpciones = CTkFrame(windows, border_color=colores["marcos"], border_width=2,
                            corner_radius=0, fg_color=colores["fondo"]
                            )
    
    logo = CTkLabel(frameOpciones, text="", image=iconos["equipo"])



    frameOpciones.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    logo.pack(padx=10, pady=10)
    formulario(windows)
    windows.mainloop()
