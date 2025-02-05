from customtkinter import CTkToplevel, CTkLabel, CTkEntry, CTkButton, CTkComboBox, CTkFrame
from tkinter import messagebox


from bk_consultas import consultarPaquetes
from bk_recursos import colores_ui, imagenes_ui
from bk_insert import insertarCliente

#variables necesarias
colores = colores_ui()
paquetes = consultarPaquetes()
iconos = imagenes_ui()
nombre_paquetes = [paquete[1] for paquete in paquetes]
dias_corte = [str(day) for day in range(1, 32)]


def enviarDatos(nombreEntry, telefonoEntry, emailEntry, direccionEntry, paquetesEntry, windows, ipClienteEntry, diaCorteEntry):
    nombre = nombreEntry.get()
    telefono = telefonoEntry.get()
    email = emailEntry.get()
    direccion = direccionEntry.get()
    paquete = paquetesEntry.get()
    ip_cliente = ipClienteEntry.get()
    dia_corte = diaCorteEntry.get()

    if not nombre or not telefono or not email or not direccion or not paquete or not ip_cliente or not dia_corte:
        messagebox.showerror("SpiderNet", "Todos los campos son necesarios")
        return
    
    enviado = insertarCliente(nombre, telefono, email, direccion, paquete, ip_cliente, dia_corte)

    if enviado:
        windows.destroy()

def formulario(windows):
    # Consultar paquetes cada vez que se abre la ventana
    paquetes = consultarPaquetes()
    nombre_paquetes = [paquete[1] for paquete in paquetes]  # Extraer solo los nombres de los paquetes


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
    
    paquetesLabel = CTkLabel(contenedorFormulario, text="Paquetes Disponibles" , font=("Arial", 20), text_color="black")

    paquetesEntry = CTkComboBox(contenedorFormulario, values=nombre_paquetes,  # Ahora usa la lista actualizada
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250)

    
    ipClienteLabel = CTkLabel(contenedorFormulario, text="Ip del Cliente" , font=("Arial", 20), text_color="black")

    ipClienteEntry = CTkEntry(contenedorFormulario,  # Ahora usa la lista actualizada
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250,
                        placeholder_text="192.168.10.254")

    diaCorteLabel = CTkLabel(contenedorFormulario, text="Dia de Corte" , font=("Arial", 20), text_color="black")

    diaCorteEntry = CTkComboBox(contenedorFormulario, values=dias_corte,  # Ahora usa la lista actualizada
                        border_color=colores["marcos"], border_width=2,
                        corner_radius=10,
                        width=250
                        )


    

    btnGuardar = CTkButton(contenedorFormulario, text="Guardar", border_color=colores["marcos"],
                        border_width=2, corner_radius=10, fg_color=colores["boton"],
                        text_color="black",
                        width=250,
                        command=lambda:enviarDatos(nombreEntry, telefonoEntry, emailEntry, direccionEntry, paquetesEntry, windows, ipClienteEntry,
                                                diaCorteEntry))


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
    ipClienteLabel.grid(column=1, row=4, padx=10, pady=10)
    paquetesEntry.grid(column=0, row=5, padx=10, pady=10)
    ipClienteEntry.grid(column=1, row=5, padx=10, pady=10)
    diaCorteLabel.grid(column=0, row=6, padx=10, pady=10)
    diaCorteEntry.grid(column=0, row=7, padx=10, pady=10)
    btnGuardar.grid(column=1, row=7, padx=10, pady=10)


    return paquetesEntry  # Devolver el ComboBox para poder actualizarlo después si es necesario


def nuevoCliente():
    windows = CTkToplevel()
    windows.title("Nuevo Cliente")
    windows.geometry("800x400")
    windows.resizable(False, False)

    contenedorOpciones = CTkFrame(windows, border_color=colores["marcos"], border_width=2,
                                corner_radius=0, fg_color=colores["fondo"])
    
    icono = CTkLabel(contenedorOpciones, text="", image=iconos["cliente"])

    contenedorOpciones.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    icono.pack(padx=10, pady=10)

    # Llamamos a la función formulario para que consulte los paquetes en tiempo real
    formulario(windows)

    windows.mainloop()
