from customtkinter import CTkEntry, CTkLabel, CTkButton, CTkToplevel, CTkComboBox
from tkinter import messagebox
from bk_recursos import colores_ui
from bk_bloquear_cliente import bloquear_ip, desbloquear_ip
from bk_consultas import consultar_microtiks, consultar_ip_microtik, consultar_ip_cliente

colores = colores_ui()

def get_datos(id, microtik, windows):
    microtik = microtik.get()
    ip_cliente = consultar_ip_cliente(id)
    ip_microtik = consultar_ip_microtik(nombre=microtik)

    if ip_cliente:
        if ip_microtik:
            if bloquear_ip(host=ip_microtik[0], user=ip_microtik[1], password=ip_microtik[2], ip_bloqueo=ip_cliente[0], id=id):
                windows.destroy()
                messagebox.showinfo("SpiderNet", "El cliente se bloqueo con exito")
        else:
            windows.destroy()
            messagebox.showerror("SpiderNet", "Hubo un error, verifica los datos")

def get_desbloqueo(id, microtik, windows):
    microtik = microtik.get()
    ip_cliente = consultar_ip_cliente(id)
    ip_microtik = consultar_ip_microtik(nombre=microtik)

    if ip_cliente:
        if ip_microtik:
            if desbloquear_ip(host=ip_microtik[0], user=ip_microtik[1], password=ip_microtik[2], ip_bloqueo=ip_cliente[0], id=id):
                windows.destroy()
                messagebox.showinfo("SpiderNet", "El cliente se desbloqueo con exito")
        else:
            windows.destroy()
            messagebox.showerror("SpiderNet", "Hubo un error, verifica los datos")


def panel_bloqueo(id, nombreCliente):
    microtiks_disponibles = consultar_microtiks()
    nombre_microtiks = [paquetes[1] for paquetes in microtiks_disponibles]

    windows = CTkToplevel()
    windows.title("Bloqueo de cliente")
    windows.geometry("550x200")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    nombreLabel = CTkLabel(windows, text="Nombre del cliente", font=("Arial", 16), text_color="white")
    nombreEntry = CTkEntry(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        text_color="white",
                        width=250)
    
    microtikLabel = CTkLabel(windows, text="Servidor MicroTik", font=("Arial", 16), text_color="white")
    microtik = CTkComboBox(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        text_color="white", values=nombre_microtiks,
                        width=250)
    
    btnBloquear = CTkButton(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color="red", text="Bloquear", text_color="black",
                            width=250,
                            command=lambda:get_datos(id, microtik, windows))

    
    btnDesbloquear = CTkButton(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color="blue", text="Desbloquear", text_color="white",
                            width=250,
                            command=lambda:get_desbloqueo(id, microtik, windows))
    
    nombreLabel.grid(column=0, row=0, padx=10, pady=10)
    microtikLabel.grid(column=1, row=0, padx=10, pady=10)
    nombreEntry.grid(column=0, row=1, padx=10, pady=10)
    microtik.grid(column=1, row=1, padx=10, pady=10)
    btnBloquear.grid(column=0, row=2, padx=10, pady=10)
    btnDesbloquear.grid(column=1, row=2, padx=10, pady=10)

    nombreEntry.insert(0, nombreCliente)
    windows.mainloop()
