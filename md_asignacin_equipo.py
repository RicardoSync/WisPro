from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkLabel, CTkComboBox, CTkFrame
from tkinter import messagebox

from bk_recursos import colores_ui, imagenes_ui
from bk_insert import insertarEquipo

colores = colores_ui()
iconos = imagenes_ui()
tipo_equipo = ["Router", "Antena", "ONU", "Otro"]
tipo_estado = ["Rentado", "Vendido", "Propio", "Almacenado"]

def enviarEquipos(nombreEquipoEntry, tipoEquipo, marcaEquipo, modeloEquipo, macEquipo, numeroSerialEquipo, estadoEquipo, id_cliente, ventana):
    nombre = nombreEquipoEntry.get()
    tipo = tipoEquipo.get()
    marca = marcaEquipo.get()
    modelo = modeloEquipo.get()
    mac = macEquipo.get()
    serial = numeroSerialEquipo.get()
    estado = estadoEquipo.get()

    if insertarEquipo(nombre, tipo, marca, modelo, mac, serial, estado, id_cliente):
        messagebox.showinfo("SpiderNet", "Asignacion lista")
        ventana.destroy()

def formularioEquipo(ventana, id_cliente, nombre):
    contenedorFormulario = CTkFrame(ventana, border_color=colores["marcos"], border_width=2, 
                                corner_radius=0, fg_color=colores["fondo"]
                                )
    

    nombreEquipoEntry = CTkEntry(contenedorFormulario, placeholder_text="Nombre equipo",
                                border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white",
                                text_color="black",
                                width=200,
                                height=30)
    
    tipoEquipo = CTkComboBox(contenedorFormulario, values=tipo_equipo,
                                border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white",
                                text_color="black",
                                width=200,
                                height=30)
    
    marcarEquipo = CTkEntry(contenedorFormulario, placeholder_text="Marca del equipo",
                                border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white",
                                text_color="black",
                                width=200,
                                height=30)
    
    modeloEquipo = CTkEntry(contenedorFormulario, placeholder_text="Modelo equipo",
                                border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white",
                                text_color="black",
                                width=200,
                                height=30)
    
    macEquipo = CTkEntry(contenedorFormulario, placeholder_text="Mac Addres",
                                border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white",
                                text_color="black",
                                width=200,
                                height=30)
    
    numeroSerialEquipo = CTkEntry(contenedorFormulario, placeholder_text="No Serial Equipo",
                                border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white",
                                text_color="black",
                                width=200,
                                height=30)
    
    estadoEquipo = CTkComboBox(contenedorFormulario, values=tipo_estado,
                                border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white",
                                text_color="black",
                                width=200,
                                height=30)
    
    btnAsignar = CTkButton(contenedorFormulario, text="Asignar Equipo", border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white", text_color="black",
                                width=200,
                                height=30,
                                command=lambda:enviarEquipos(nombreEquipoEntry, tipoEquipo, marcarEquipo, modeloEquipo, macEquipo,
                                                            numeroSerialEquipo, estadoEquipo, id_cliente, ventana))

    btnCancelar = CTkButton(contenedorFormulario, text="Cancelar", border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white", text_color="black",
                                width=200,
                                height=30,
                                command=ventana.destroy)


    contenedorFormulario.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    nombreEquipoEntry.grid(column=0, row=0, padx=10, pady=10)
    tipoEquipo.grid(column=1, row=0, padx=10, pady=10)
    marcarEquipo.grid(column=2, row=0, padx=10, pady=10)
    modeloEquipo.grid(column=0, row=1, padx=10, pady=10)
    macEquipo.grid(column=1, row=1, padx=10, pady=10)
    numeroSerialEquipo.grid(column=2, row=1, padx=10, pady=10)
    estadoEquipo.grid(column=0, row=2, padx=10, pady=10)
    btnAsignar.grid(column=0, row=3, padx=10, pady=10)
    btnCancelar.grid(column=1, row=3, padx=10, pady=10)

def asignacionEquipo(id_cliente, nombre):
    ventana = CTkToplevel()
    ventana.title(f"Asignacion equipo {nombre}")
    ventana.geometry("900x200")
    ventana.resizable(False, False)
    ventana.configure(fg_color=colores["fondo"])
    #frame contenedor
    contenedorImagen = CTkFrame(ventana, border_color=colores["marcos"], border_width=2,
                                corner_radius=0, fg_color=colores["fondo"])
    
    imagen = CTkLabel(contenedorImagen, text="", image=iconos["equipo"])
    


    #posicion del elementos
    contenedorImagen.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    imagen.pack(padx=10, pady=10)
    formularioEquipo(ventana, id_cliente, nombre)
    ventana.mainloop()

