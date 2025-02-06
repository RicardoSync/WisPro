from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkEntry
from bk_recursos import colores_ui, imagenes_ui
from bk_consultas import detalles_cliente
colores = colores_ui()
iconos = imagenes_ui()


def detalles_cliente(id, nombre, telefono, email, direccion, fechaRegistro, ipPaquete, ipCliente, diaCorte):
    windows = CTkToplevel()
    windows.title(f"Detalles del cliente {nombre}")
    windows.geometry("400x600")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    cliente = CTkLabel(windows, text="", image=iconos["cliente"])

    nombreLabel = CTkLabel(windows, text=f"Nombre: {nombre}", text_color="white", font=("Arial", 18))
    telefonoLabel = CTkLabel(windows, text=f"Telefono: {telefono}", text_color="white", font=("Arial", 18))
    emailLabel = CTkLabel(windows, text=f"Email: {email}", text_color="white", font=("Arial", 18))
    direccionLabel = CTkLabel(windows, text=f"Direccion: {direccion}", text_color="white", font=("Arial", 18))
    fechaRegistroLabel = CTkLabel(windows, text=f"Instalacion: {fechaRegistro}", text_color="white", font=("Arial", 18))
    idPaqueteLabel = CTkLabel(windows, text=f"Paquete Actual: {ipPaquete}", text_color="white", font=("Arial", 18))
    ipClienteLabel = CTkLabel(windows, text=f"Ip del Cliente: {ipCliente}", text_color="white", font=("Arial", 18))
    diaCorteLabel = CTkLabel(windows, text=f"Dia de corte: {diaCorte}", text_color="white", font=("Arial", 18))

    nombreLabel.pack(padx=10, pady=10)
    telefonoLabel.pack(padx=10, pady=10)
    emailLabel.pack(padx=10, pady=10)
    direccionLabel.pack(padx=10, pady=10)
    fechaRegistroLabel.pack(padx=10, pady=10)
    idPaqueteLabel.pack(padx=10, pady=10)
    ipClienteLabel.pack(padx=10, pady=10)
    diaCorteLabel.pack(padx=10, pady=10)
    windows.mainloop()

