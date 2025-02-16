"""
Este modulo debe perdir al usuario lo sigeuite:
    1 - Nombre del ISP
    2 - Numero de telefono
    3 - Correo electronico

Con eso vamos a buscar la base de datso y devolver para poder almacenarlo dentro del json
"""
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
from bk_recursos import colores_ui, imagenes_ui
from bk_creacion_cuenta import obtener_database
from tkinter import messagebox
import json

colores = colores_ui()
iconos = imagenes_ui()

def obtener_datos(nombreentry, telefonoEntry, correoEntry, btnGO):
    nombre = nombreentry.get()
    telefono = telefonoEntry.get()
    correo = correoEntry.get()

    if not nombre or not telefono or not correo:
        messagebox.showwarning("SpiderNet", "Todos los campos son necesarios")
        return
    
    database = obtener_database(nombre, telefono, correo)
    
    if database:
        # Datos base para la configuración
        config = {
            "host": "servidores_escobedo",
            "port": 3389,
            "user": "usuario_escobedo",
            "password": "password_escobed",
            "database": database[0]
        }

        # Guardar en un archivo JSON
        with open("config.json", "w") as file:
            json.dump(config, file, indent=4)
        messagebox.showinfo("SpiderNet", "Ya encontramos tu cuenta, ahora puedes iniciar sesion en el sistema")
        btnGO.pack(padx=10, pady=10)


    elif database == None:
        messagebox.showwarning("SpiderNet","Por favor ingresa el nombre de tu isp, el telefono y correo electronico con el que se creo la cuenta")
    else:
        messagebox.showerror("SpiderNet", "No logramos obtener los datos")

def inicioSesion(ventana):
    from md_login_cuenta import inicioSesion
    inicioSesion(windows=ventana)


def md_cuenta_existente(windows):
    windows.destroy()
    ventana = CTk()
    ventana.title("Inicio de Sesión")
    ventana.geometry("400x650")
    ventana.resizable(False, False)
    ventana.configure(fg_color=colores["fondo"])

    formulario = CTkFrame(ventana, border_color=colores["marcos"], border_width=2, corner_radius=6)
    icono = CTkLabel(formulario, text="", image=iconos["logo"])

    nombreLabel = CTkLabel(formulario, text="Nombre de ISP", text_color="white", font=("Arial", 15))

    nombreentry = CTkEntry(formulario, placeholder_text="DOBLENET", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, width=300)
    
    telefonoLabel = CTkLabel(formulario, text="Telefono Celular", text_color="white", font=("Arial", 15))
    telefonoEntry = CTkEntry(formulario, placeholder_text="498142266", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, width=300)


    correoLabel = CTkLabel(formulario, text="Correo Electronico", text_color="white", font=("Arial", 15))
    correoEntry = CTkEntry(formulario, placeholder_text="richardobedoesc@gmail.com", border_color=colores["marcos"], border_width=2,
                        corner_radius=6, width=300)

    btnInicio = CTkButton(formulario, text="Buscar Cuenta", text_color="black", border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"],
                        command=lambda:obtener_datos(nombreentry, telefonoEntry, correoEntry, btnGO))

    btnGO = CTkButton(formulario, text="Iniciar Sesion", text_color="black", border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"],
                        command=lambda:inicioSesion(ventana))
    
    nota = CTkLabel(formulario, text="Ingresa los mismos datos\ncuando creaste tu cuenta por favor!",
                    text_color="white", font=("Arial", 15)
                    )
    
    formulario.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
    icono.pack(padx=10, pady=10)
    nota.pack(padx=10, pady=10)
    nombreLabel.pack(padx=10, pady=10)
    nombreentry.pack(padx=10, pady=10)
    telefonoLabel.pack(padx=10, pady=10)
    telefonoEntry.pack(padx=10, pady=10)
    correoLabel.pack(padx=10, pady=10)
    correoEntry.pack(padx=10, pady=10)
    btnInicio.pack(padx=10, pady=10)
    ventana.mainloop()
