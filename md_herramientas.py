import threading
import os
import time
from tkinter import messagebox
from customtkinter import CTkToplevel, CTkButton
from md_pruebas_red import md_enviar_ping
from generar_clientes import md_generacion
from bk_recursos import colores_ui, imagenes_ui

# Aquí asumimos que ya tienes tu configuración de colores y iconos
iconos = imagenes_ui()
colores = colores_ui()

# Variable global para controlar el ping
ping_activo = False
ping_thread = None

def ping_a_ip(ip):
    global ping_activo
    while ping_activo:
        # Ejecutamos el comando de ping usando el sistema operativo
        respuesta = os.system(f"ping -n 1 {ip}")
        
        # Si el ping falla (respuesta diferente a 0)
        if respuesta != 0:
            messagebox.showwarning("Ping Fallido", f"No se pudo conectar a {ip}.")
        
        # Esperar 1 segundo antes de volver a hacer ping
        time.sleep(1)

def iniciar_ping():
    global ping_activo, ping_thread
    if not ping_activo:
        ping_activo = True
        ping_thread = threading.Thread(target=ping_a_ip, args=("8.8.8.8",))
        ping_thread.start()
    else:
        messagebox.showinfo("Ping", "El ping ya está activo.")

def detener_ping():
    global ping_activo, ping_thread
    if ping_activo:
        ping_activo = False
        ping_thread.join()  # Espera a que el hilo termine antes de continuar
        messagebox.showinfo("Ping Detenido", "El ping ha sido detenido.")
    else:
        messagebox.showinfo("Ping", "El ping no está activo.")

def md_herramentas():
    windows = CTkToplevel()
    windows.title("Herramientas del Sistema")
    windows.geometry("700x600")
    windows.resizable(False, False)
    windows.configure(fg_color=colores["fondo"])

    btnPing = CTkButton(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Ping", text_color="black",
                        image=iconos["ping"],
                        command=md_enviar_ping)
    
    btnGeneracion = CTkButton(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color=colores["boton"], text="Generar Datos", text_color="black",
                            image=iconos["auto"],
                            command=md_generacion)
    
    btnWhatsappBot = CTkButton(windows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                                    fg_color=colores["boton"], text="WhatsApp Bot", text_color="black",
                                    image=iconos["auto"],
                                    command=lambda:messagebox.showinfo("SpiderNet", "Proximamente integraremos las notificaciones via whatsapp"))
    

    
    btnPing.grid(column=0, row=0, padx=10, pady=10)
    btnGeneracion.grid(column=1, row=0, padx=10, pady=10)
    btnWhatsappBot.grid(column=2, row=0, padx=10, pady=10)

    windows.mainloop()
