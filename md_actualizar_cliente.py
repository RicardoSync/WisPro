from customtkinter import CTkToplevel, CTkLabel, CTkEntry, CTkButton, CTkComboBox, CTkFrame
from tkinter import messagebox


from bk_consultas import consultarPaquetes
from bk_recursos import colores_ui, imagenes_ui

#variables necesarias
colores = colores_ui()
paquetes = consultarPaquetes()
nombre_paquetes = [paquete[1] for paquete in paquetes]
iconos = imagenes_ui()

def insertarElementos(nombreEntry, telefonoEntry, emailEntry, direccionEntry, paquetesEntry, nombre, telefono, email, direccion, paquete):
    nombreEntry.insert(0, nombre)
    telefonoEntry.insert(0, telefono)
    emailEntry.insert(0, email)
    direccionEntry.insert(0, direccion)
    paquetesEntry.insert(0, paquete)


def formulario(nombre, telefono, email, direccion, paquete, windows):
    contenedorFormulario = CTkFrame(windows, border_color=colores["marcos"], border_width=2,
                                corner_radius=0, fg_color=colores["fondo"])
    
    nombreLabel = CTkLabel(contenedorFormulario, text="Nombre", font=("Arial", 20), text_color="black")

    nombreEntry = CTkEntry(contenedorFormulario, placeholder_text="Ricardo Escobedo",
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250)
    
    telefonoLabel = CTkLabel(contenedorFormulario, text="Telefono", font=("Arial", 20), text_color="black")

    telefonoEntry = CTkEntry(contenedorFormulario, placeholder_text="+52 9802325090",
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250)

    emailLabel = CTkLabel(contenedorFormulario, text="Correo Electronico" , font=("Arial", 20), text_color="black")

    emailEntry = CTkEntry(contenedorFormulario, placeholder_text="ricardoescobedo@spidernet.com",
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250)

    direccionLabel = CTkLabel(contenedorFormulario, text="Direccion" , font=("Arial", 20), text_color="black")

    direccionEntry = CTkEntry(contenedorFormulario, placeholder_text="Siempre Viva 203",
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250)
    
    paquetesLabel = CTkLabel(contenedorFormulario, text="Paquetes Actual" , font=("Arial", 20), text_color="black")

    paquetesEntry = CTkEntry(contenedorFormulario,
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250)

    paqueteNuevo = CTkLabel(contenedorFormulario, text="Paquetes Nuevo" , font=("Arial", 20), text_color="black")

    paqueteNuevoEntry = CTkComboBox(contenedorFormulario, values=nombre_paquetes,
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250)
    
    btnGuardar = CTkButton(contenedorFormulario, text="Actualizar", border_color=colores["marcos"],
                        border_width=2, corner_radius=10, fg_color=colores["boton"],
                        text_color="black",
                        width=250)

    btnCancelar = CTkButton(contenedorFormulario, text="Cancelar", border_color=colores["marcos"],
                        border_width=2, corner_radius=10, fg_color=colores["boton"],
                        text_color="black",
                        command=windows.destroy,
                        width=250
                        )
    
    contenedorFormulario.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    nombreLabel.grid(column=0, row=0, padx=20, pady=10)
    telefonoLabel.grid(column=1, row=0, padx=20, pady=10)
    nombreEntry.grid(column=0, row=1, padx=20, pady=10)
    telefonoEntry.grid(column=1, row=1, padx=20, pady=10)
    emailLabel.grid(column=0, row=2, padx=10, pady=10)
    direccionLabel.grid(column=1, row=2, padx=10, pady=10)
    emailEntry.grid(column=0, row=3, padx=10, pady=10)
    direccionEntry.grid(column=1, row=3, padx=10, pady=10)
    paquetesLabel.grid(column=0, row=4, padx=10, pady=10)
    paqueteNuevo.grid(column=1, row=4, padx=10, pady=10)
    paquetesEntry.grid(column=0, row=5, padx=10, pady=10)
    paqueteNuevoEntry.grid(column=1, row=5, padx=10, pady=10)
    btnGuardar.grid(column=0, row=6, padx=10, pady=10)
    btnCancelar.grid(column=1, row=6, padx=10, pady=10)
    insertarElementos(nombreEntry, telefonoEntry, emailEntry, direccionEntry, paquetesEntry, nombre,
                    telefono, email, direccion, paquete)

def actualizarCliente(nombre, telefono, email, direccion, paquete):
    windows = CTkToplevel()
    windows.title("Actualizar Cliente")
    windows.geometry("800x400")
    windows.resizable(False, False)
    windows._set_appearance_mode("dark")

    contenedorOpciones = CTkFrame(windows, border_color=colores["marcos"], border_width=2,
                                corner_radius=0, fg_color=colores["fondo"])
    
    icono = CTkLabel(contenedorOpciones, text="", image=iconos["cliente"])
    

    contenedorOpciones.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    icono.pack(padx=10, pady=10)
    formulario(nombre, telefono, email, direccion, paquete, windows)
    windows.mainloop()

