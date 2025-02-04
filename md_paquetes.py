from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkFrame, CTkLabel
from tkinter import ttk, messagebox, END
import tkinter as tk

from bk_recursos import colores_ui
from bk_consultas import consultarPaquetes
from bk_insert import insertarPaquete
from bk_delete import eliminarPaquete
from md_actualizar_paquetes import actualizarPaquetes
colores = colores_ui()


def enviarEliminacion(tabla, windows):
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showerror("SpiderNet", "Selecciona un usuario para poder eliminarlo")
    
    identificador = tabla.item(seleccionado, "values")
    id = identificador[0]

    if messagebox.askyesno("SpiderNet", "Seguro que quieres eliminar el paquete?"):
        eliminarPaquete(id)
        tablaPaquetes(windows)
    else:
        messagebox.showinfo("SpiderNet", "No eliminamos ningun elemento")

def enviarActializacion(tabla, windows):
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showinfo("SpiderNet", "No podemos actualizar sin ningun dato")
    
    identificador = tabla.item(seleccionado, "values")
    id = identificador[0]
    nombre = identificador[1]
    velocidad = identificador[2]
    precio = identificador[3]

    actualizarPaquetes(id, nombre, velocidad, precio)
    tablaPaquetes(windows)

def getDatos(nombreEntryPaquete, velocidadEntry, precioEntry, windows):
    nombre = nombreEntryPaquete.get()
    velocidad = velocidadEntry.get()
    precio = precioEntry.get()

    if not nombre or not velocidad or not precio:
        messagebox.showerror("SpiderNet", "Todos los campos son obligatorios")
        return

    insertarPaquete(nombre, velocidad, precio)
    #messagebox.showinfo("SpiderNet", "Usuario registrado exitosamente")
    tablaPaquetes(windows)

def formularioUI(formBanner, windows):

    nombrePaqueteLabel = CTkLabel(formBanner, text="Nombre Completo", font=("Arial", 18, "bold"), text_color="black")

    nombreEntryPaquete = CTkEntry(formBanner, placeholder_text="Plan Basico", border_width=2,
                        border_color=colores["marcos"], corner_radius=10,
                        width=200)
    
    velocidadLabel = CTkLabel(formBanner, text="Velocidad paquete (0M/0M)", font=("Arial", 18, "bold"), text_color="black")

    velocidadEntry = CTkEntry(formBanner, placeholder_text="100M/20M", border_width=2,
                        border_color=colores["marcos"], corner_radius=10,
                        width=200)
    
    precioLabel = CTkLabel(formBanner, text="Precio", font=("Arial", 18, "bold"), text_color="black")

    precioEntry = CTkEntry(formBanner, border_width=2,
                        border_color=colores["marcos"], corner_radius=10,
                        width=200)

    btnRegistrar  = CTkButton(formBanner, text="Registrar", border_width=2, border_color=colores["marcos"],
                            corner_radius=10, fg_color=colores["boton"],
                            width=200,
                            text_color="black",
                            command=lambda:getDatos(nombreEntryPaquete, velocidadEntry, precioEntry, windows)
                            )

    btnCancelar  = CTkButton(formBanner, text="Cancelar", border_width=2, border_color=colores["marcos"],
                            corner_radius=10, fg_color=colores["boton"],
                            width=200,
                            text_color="black",
                            command=windows.destroy)

    nombrePaqueteLabel.pack(padx=10, pady=10)
    nombreEntryPaquete.pack(padx=10, pady=10)
    velocidadLabel.pack(padx=10, pady=10)
    velocidadEntry.pack(padx=10, pady=10)
    precioLabel.pack(padx=10, pady=10)
    precioEntry.pack(padx=10, pady=10)
    btnRegistrar.pack(padx=10, pady=10)
    btnCancelar.pack(padx=10, pady=10)

def tablaPaquetes(windows):
    paquetesDisponibles = consultarPaquetes()

    contenedorTabla = CTkFrame(windows, border_width=2, border_color=colores["marcos"],
                        corner_radius=0, fg_color=colores["fondo"])
    

    tabla = ttk.Treeview(contenedorTabla, columns=("ID", "Nombre", "Velocidad", "Precio"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Velocidad", text="Velocidad")
    tabla.heading("Precio", text="Precio")


    contenedorTabla.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    tabla.pack(expand=True, fill="both")

    for item in tabla.get_children():
        tabla.delete(item)

    for paquetes in paquetesDisponibles:
        tabla.insert("", END, values=paquetes)

    #creacion del menu contextual
    menu = tk.Menu(tabla, tearoff=0)
    menu.add_command(label="Editar", command=lambda:enviarActializacion(tabla, windows))
    menu.add_command(label="Eliminar", command=lambda:enviarEliminacion(tabla, windows))
    menu.add_command(label="Actualizar", command=lambda:tablaPaquetes(windows))


    def mostrar_menu(event):
        seleccion = tabla.selection()
        if seleccion:  # Solo mostrar menú si hay un ítem seleccionado
            menu.post(event.x_root, event.y_root)

    tabla.bind("<Button-3>", mostrar_menu)  # Evento clic derecho

def creacionPaquetes(): 
    windows = CTkToplevel()
    windows.title("Nuevo Paquete")
    windows.geometry("1280x800")
    windows.resizable(False, False)


    #creamos el banner de formulario
    formBanner = CTkFrame(windows, border_width=2, border_color=colores["marcos"],
                        corner_radius=0, fg_color=colores["fondo"])
    

    
    #posicion de elementos
    formBanner.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    formularioUI(formBanner, windows)
    tablaPaquetes(windows)
    windows.mainloop()