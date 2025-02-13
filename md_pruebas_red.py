from customtkinter import CTkToplevel, CTkEntry, CTkLabel, CTkButton, CTkTextbox, CTkFrame
from bk_recursos import colores_ui
from tkinter import messagebox
from bk_ping import enviar_pint
import subprocess
import platform
colores = colores_ui()


def enviar_ping(ipEntry, salidaComando, numRepeticiones):
    ip = ipEntry.get()
    repeticiones = numRepeticiones.get()
    if not ip or not repeticiones:
        messagebox.showerror("SpiderNet", "Para poder inicar la prueba, ingresa la IP de destino")
        return
    ping_exitoso = enviar_pint(host=ip, repeticiones=repeticiones)

    if ping_exitoso:
        salidaComando.insert("end", f"El host {ip} esta respondiendo de manera correcta ✅" + "\n")
        salidaComando.see("end")  # Hace scroll automático al final
        salidaComando.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)
    else:
        salidaComando.insert("end", f"El host {ip} esta no responde de manera correcta ❌" + "\n")
        salidaComando.see("end")  # Hace scroll automático al final
        salidaComando.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)

def enviar_ping_manual(ip, salidaComando):
    if not ip:
        messagebox.showerror("SpiderNet", "Para poder inicar la prueba, ingresa la IP de destino")
        return
    ping_exitoso = enviar_pint(host=ip)

    if ping_exitoso:
        salidaComando.insert("end", f"El host {ip} esta respondiendo de manera correcta ✅" + "\n")
        salidaComando.see("end")  # Hace scroll automático al final
        salidaComando.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)
    else:
        salidaComando.insert("end", f"El host {ip} esta no responde de manera correcta ❌" + "\n")
        salidaComando.see("end")  # Hace scroll automático al final
        salidaComando.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)  

def md_enviar_ping():
    windows = CTkToplevel()
    windows.title("Pruebas de PING")
    windows.geometry("600x800")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    #frame entrada
    frameEntrada = CTkFrame(windows, border_color=colores["marcos"], border_width=2, corner_radius=6)
    lbl = CTkLabel(frameEntrada, text="Ingresa la IP",
                                        text_color="white",
                                        font=("Arial", 15))

    salidaComando = CTkTextbox(windows, border_color=colores["marcos"], border_width=2, corner_radius=6)


    ipEntry = CTkEntry(frameEntrada, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        text_color="white", placeholder_text="8.8.8.8", width=150)
    
    numRepeticiones = CTkEntry(frameEntrada, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        text_color="white", width=150)
    
    btnInicio = CTkButton(frameEntrada, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Iniciar", text_color="black",
                        width=100,
                        command=lambda:enviar_ping(ipEntry, salidaComando, numRepeticiones))

    btnGoogle = CTkButton(frameEntrada, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Google", text_color="black",
                        width=100,
                        command=lambda:enviar_ping_manual(ip="8.8.8.8", salidaComando=salidaComando))  

    btnCloudflare = CTkButton(frameEntrada, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Cloudflare", text_color="black",
                        width=100,
                        command=lambda:enviar_ping_manual(ip="1.1.1.1", salidaComando=salidaComando, numRepeticiones=numRepeticiones))  

    numRepeticiones.insert(0, "5")
    frameEntrada.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.2)
    lbl.grid(column=0, row=0, padx=10, pady=10)
    ipEntry.grid(column=1, row=0, padx=10, pady=10)
    numRepeticiones.grid(column=2, row=0, padx=10, pady=10)
    btnInicio.grid(column=1, row=1, padx=10, pady=10)
    windows.mainloop()
