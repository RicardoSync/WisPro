from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkComboBox, CTkLabel
from bk_recursos import colores_ui
from bk_update import actualizarPaquete
from tkinter import messagebox

colores = colores_ui()

def insertarElementos(nombreEntry, velocidadEnrty, precioEntry, nombre, velocidad, precio):
        # Insertar los valores en los campos de entrada
        nombreEntry.delete(0, "end")  # Limpiar antes de insertar
        velocidadEnrty.delete(0, "end")
        precioEntry.delete(0, "end")

        nombreEntry.insert(0, nombre)
        velocidadEnrty.insert(0, velocidad)
        precioEntry.insert(0, precio)

def enviarDatos(id, nombreEntry, velocidadEnrty, precioEntry, panel):
    nombre = nombreEntry.get()
    velocidad = velocidadEnrty.get()
    precio = precioEntry.get()

    if not nombre or not velocidad or not precio:
        messagebox.showerror("SpiderNet", "No podemos actualizar si faltan datos")
        return
    
    actualizarPaquete(id, nombre, velocidad, precio)
    panel.destroy()
    

def actualizarPaquetes(id, nombre, velocidad, precio):
    panel = CTkToplevel()
    panel.title(f"Actualizar Paquete {nombre}")
    panel.geometry("600x500")
    panel.resizable(False, False)
    panel._set_appearance_mode("dark")



    nombreLabel = CTkLabel(panel, text="Nombre del Paquete", font=("Arial", 20, "bold"), text_color="white")
    velocidadLabel = CTkLabel(panel, text="Velocidad", font=("Arial", 20, "bold"), text_color="white")
    precioLabel = CTkLabel(panel, text="Precio", font=("Arial", 20, "bold"), text_color="white")

    nombreEntry = CTkEntry(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320)
    velocidadEnrty = CTkEntry(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320)
    precioEntry = CTkEntry(panel, border_width=2, border_color=colores["marcos"], corner_radius=10, width=320)

    
    btnActualizar = CTkButton(panel, text="Actualizar", border_color=colores["marcos"],
                            border_width=2, corner_radius=10, width=320,
                            fg_color=colores["boton"],
                            text_color="black",
                            command=lambda:enviarDatos(id, nombreEntry, velocidadEnrty, precioEntry, panel)
                            ) 
    
    btnCanelar = CTkButton(panel, text="Cancelar", border_color=colores["marcos"],
                            border_width=2, corner_radius=10, width=320,
                            command=panel.destroy,
                            fg_color=colores["boton"],
                            text_color="black")



    nombreLabel.pack(padx=10, pady=10)
    nombreEntry.pack(padx=10, pady=10)
    velocidadLabel.pack(padx=10, pady=10)
    velocidadEnrty.pack(padx=10, pady=10)
    precioLabel.pack(padx=10, pady=10)
    precioEntry.pack(padx=10, pady=10)
    btnActualizar.pack(padx=10, pady=10)
    btnCanelar.pack(padx=10, pady=10)
    insertarElementos(nombreEntry, velocidadEnrty, precioEntry, nombre, velocidad, precio)
    panel.mainloop()