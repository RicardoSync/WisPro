from customtkinter import CTkToplevel, CTkEntry, CTkButton, CTkLabel, CTkComboBox, CTkFrame
from tkinter import messagebox

from bk_recursos import colores_ui, imagenes_ui
from bk_update import actualizacion_equipo

colores = colores_ui()
iconos = imagenes_ui()


def insertarElementos(nombreEquipoEntry, tipoEquipo, marcarEquipo, modeloEquipo, macEquipo, numeroSerialEquipo,estadoEquipo, id, ventana):
    nombre = nombreEquipoEntry.get()
    tipo = tipoEquipo.get()
    marca = marcarEquipo.get()
    modelo = modeloEquipo.get()
    mac = macEquipo.get()
    serial = numeroSerialEquipo.get()
    estado = estadoEquipo.get()

    if actualizacion_equipo(nombre, tipo, marca, modelo, mac, serial, estado, id):
        ventana.destroy()

def editar_equipo_windows(nombre, tipo_equipo_obtenido, marca, modelo, mac, serial, estado_equipo_obtenido, id):
    tipo_equipo = ["Router", "Antena", "ONU", "Otro"]
    tipo_estado = ["Rentado", "Vendido", "Propio"]


    # Insertar en la primera posición (índice 0)
    tipo_equipo.insert(0, tipo_equipo_obtenido)
    tipo_estado.insert(0, estado_equipo_obtenido)

    ventana = CTkToplevel()
    ventana.title("Editar Equipo")
    ventana.geometry("900x200")
    ventana.resizable(False, False)

    #frame contenedor
    contenedorImagen = CTkFrame(ventana, border_color=colores["marcos"], border_width=2,
                                corner_radius=0, fg_color=colores["fondo"])
    
    imagen = CTkLabel(contenedorImagen, text="", image=iconos["equipo"])
    
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
    
    # Configurar el ComboBox con las nuevas listas
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
        
    btnAsignar = CTkButton(contenedorFormulario, text="Actualizar Equipo", border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white", text_color="black",
                                width=200,
                                height=30,
                                command=lambda:insertarElementos(nombreEquipoEntry, tipoEquipo, marcarEquipo, modeloEquipo, macEquipo, numeroSerialEquipo,estadoEquipo, id, ventana))
    

    btnCancelar = CTkButton(contenedorFormulario, text="Cancelar", border_color=colores["marcos-xp"],
                                border_width=2, corner_radius=6,
                                fg_color="white", text_color="black",
                                width=200,
                                height=30,
                                command=ventana.destroy)

    nombreEquipoEntry.insert(0, nombre)
    marcarEquipo.insert(0, marca)
    modeloEquipo.insert(0, modelo)
    macEquipo.insert(0, mac)
    numeroSerialEquipo.insert(0, serial)

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

    #posicion del elementos
    contenedorImagen.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    imagen.pack(padx=10, pady=10)
    ventana.mainloop()

