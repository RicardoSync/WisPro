from customtkinter import CTkToplevel, CTkLabel, CTkButton, CTkComboBox, CTkTextbox
from bk_recursos import colores_ui
from bk_consultas import consultarClientes, consultar_ips_clientes
from bk_bloquear_cliente import bloquear_clientes_ips, desbloquear_clientes_ips
from tkinter import messagebox
from bk_consultas import consultar_microtiks_bloqueos, consultar_microtiks

colores = colores_ui()

def log_message(textbox, message):
    """Agrega mensajes al cuadro de texto de logs"""
    textbox.insert("end", message + "\n")
    textbox.see("end")  # Hace scroll automático al final

def bloque_por_dia(diaCorte, microtik, log_textbox):
    microtik = microtik.get()
    dia = diaCorte.get()
    datos_microtik = consultar_microtiks_bloqueos(nombre=microtik)

    if datos_microtik:
        user = datos_microtik[2]
        host = datos_microtik[3]
        password = datos_microtik[4]
        ips_clientes = consultar_ips_clientes(dia_corte=dia)

        for ips in ips_clientes:
            id_clientes = ips[0]
            ips_disponibles = ips[1]

            exito_bloqueo = bloquear_clientes_ips(host, user, password, ip_bloqueo=ips_disponibles, id_cliente=id_clientes)

            if exito_bloqueo:
                log_message(log_textbox, f"✅ IP {ips_disponibles} bloqueada con éxito.")
            else:
                log_message(log_textbox, f"❌ Error al bloquear la IP {ips_disponibles} del cliente {id_clientes}.")
    else:
        messagebox.showerror("SpiderNet", "No podemos obtener los datos del microtik")

def desbloque_por_dia(diaCorte, microtik, log_textbox):
    microtik = microtik.get()
    dia = diaCorte.get()
    datos_microtik = consultar_microtiks_bloqueos(nombre=microtik)

    if datos_microtik:
        user = datos_microtik[2]
        host = datos_microtik[3]
        password = datos_microtik[4]
        ips_clientes = consultar_ips_clientes(dia_corte=dia)

        for ips in ips_clientes:
            id_clientes = ips[0]
            ips_disponibles = ips[1]

            exito_bloqueo = desbloquear_clientes_ips(host, user, password, ip_bloqueo=ips_disponibles, id_cliente=id_clientes)

            if exito_bloqueo:
                log_message(log_textbox, f"✅ IP {ips_disponibles} desbloqueada con éxito.")
            else:
                log_message(log_textbox, f"❌ Error al desbloquear la IP {ips_disponibles} del cliente {id_clientes}.")
    else:
        messagebox.showerror("SpiderNet", "No podemos obtener los datos del microtik")

def modulo_bloqueo_desbloqueo():
    microtiks_disponibles = consultar_microtiks()
    nombre_microtiks = [paquetes[1] for paquetes in microtiks_disponibles]
    dias_corte = [str(day) for day in range(1, 32)]

    windows = CTkToplevel()
    windows.title("Bloqueo de clientes")
    windows.geometry("550x500")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    nombreLabel = CTkLabel(windows, text="Día de Corte:", font=("Arial", 16), text_color="white")
    diaCorte = CTkComboBox(windows, values=dias_corte, width=250)

    microtikLabel = CTkLabel(windows, text="Servidor MicroTik", font=("Arial", 16), text_color="white")
    microtik = CTkComboBox(windows, values=nombre_microtiks, width=250)

    btnBloquear = CTkButton(windows, fg_color="red", text="Bloquear", text_color="black",
                            width=250, command=lambda: bloque_por_dia(diaCorte, microtik, log_textbox))

    btnDesbloquear = CTkButton(windows, fg_color="blue", text="Desbloquear", text_color="white",
                            width=250, command=lambda: desbloque_por_dia(diaCorte, microtik, log_textbox))

    nota = CTkLabel(windows, text="Selecciona un día para bloquear/desbloquear\nel acceso a Internet de los clientes con esa fecha de corte.",
                    text_color="white", font=("Monospace", 14, "bold"))

    # Cuadro de texto para logs
    log_textbox = CTkTextbox(windows, wrap="word")
    log_textbox.configure(state="normal")

    # Ubicación de los elementos
    nombreLabel.grid(column=0, row=0, padx=10, pady=10)
    microtikLabel.grid(column=1, row=0, padx=10, pady=10)
    diaCorte.grid(column=0, row=1, padx=10, pady=10)
    microtik.grid(column=1, row=1, padx=10, pady=10)
    btnBloquear.grid(column=0, row=2, padx=10, pady=10)
    btnDesbloquear.grid(column=1, row=2, padx=10, pady=10)
    nota.place(relx=0.05, rely=0.0)
    log_textbox.place(relx=0.1, rely=0.30, relwidth=0.8, relheight=0.60)
    windows.mainloop()

