from customtkinter import CTkToplevel, CTkComboBox, CTkLabel, CTkFrame, CTkTextbox, CTkButton, CTkEntry
from tkinter import messagebox, ttk, END, Menu
from bk_consultas import consultar_nombre_cliente, listar_fallas, detalles_fallas
from bk_insert import insertarFalla
from bk_delete import eliminar_falla
from bk_consultas import consultarClientes
from bk_recursos import colores_ui
from bk_update import actualizar_falla
from md_fallas_resueltas import moduloFallasResueltas

colores = colores_ui()

def obtener_datos(descripcionEntry, nombreClientes, erroresEnrey, fallaWindows):
    nombre_cliente = nombreClientes.get()

    id_cliente = consultar_nombre_cliente(nombre_cliente) #obtener el id cliente
    
    if id_cliente:
        id_cliente = (id_cliente[0])
        descripcion = descripcionEntry.get("0.0", "end")
        tipo_falla = erroresEnrey.get()
        
        if insertarFalla(id_cliente, tipo_falla, descripcion, estado=0):
            messagebox.showinfo("SpiderNet", "Reporte de falla generado")
            fallaWindows.destroy()
        else:
            messagebox.showerror("SpiderNet", "No logramos generar la falla en el sistema")
            fallaWindows.destroy()

    else:
        messagebox.showerror("SpiderNet", "No encontramos ese cliente, intenta una vez mas")
        fallaWindows.destroy()

def mostrar_detalles_falla(tablaFallas, rol):
    seleccion = tablaFallas.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "Selecciona una falla para ver los detalles.")
        return
    
    identificador = tablaFallas.item(seleccion, "values")[0]  # Obtener el ID de la falla seleccionada

    # Consultar los detalles de la falla
    fallas_registradas = detalles_fallas()
    
    for falla in fallas_registradas:
        if str(falla[0]) == identificador:  # Buscar el ID en la lista de fallas
            id_falla, cliente, tipo_falla, descripcion, estado, fecha = falla
            estado_texto = ["Pendiente", "En revisión", "Solucionado"][estado]

            detallesWindow = CTkToplevel()
            detallesWindow.title(f"Detalles de la Falla #{id_falla}")
            detallesWindow.geometry("500x650")
            detallesWindow.resizable(False, False)
            detallesWindow.configure(fg_color=colores["fondo"])

            CTkLabel(detallesWindow, text="Cliente:", font=("Arial", 16, "bold"), text_color="black").pack(pady=5)
            CTkLabel(detallesWindow, text=cliente, font=("Arial", 14), text_color="black").pack(pady=5)

            CTkLabel(detallesWindow, text="Tipo de Falla:", font=("Arial", 16, "bold"), text_color="black").pack(pady=5)
            CTkLabel(detallesWindow, text=tipo_falla, font=("Arial", 14), text_color="black").pack(pady=5)

            CTkLabel(detallesWindow, text="Descripción:", font=("Arial", 16, "bold"), text_color="black").pack(pady=5)
            descripcionText = CTkTextbox(detallesWindow, width=450, height=150, wrap="word")
            descripcionText.insert("0.0", descripcion)
            descripcionText.configure(state="disabled")
            descripcionText.pack(pady=5)

            CTkLabel(detallesWindow, text="Estado actual:", font=("Arial", 16, "bold"), text_color="black").pack(pady=5)
            estadoCombo = CTkComboBox(detallesWindow, values=["Pendiente", "En revisión", "Solucionado"])
            estadoCombo.set(estado_texto)
            estadoCombo.pack(pady=5)

            CTkLabel(detallesWindow, text="Fecha de Reporte:", font=("Arial", 16, "bold"), text_color="black").pack(pady=5)
            CTkLabel(detallesWindow, text=fecha, font=("Arial", 14), text_color="black").pack(pady=5)

            def actualizar_estado(rol):
                nuevo_estado_texto = estadoCombo.get()
                estados_dic = {"Pendiente": 0, "En revisión": 1, "Solucionado": 2}
                nuevo_estado = estados_dic[nuevo_estado_texto]

                id_tecnico = rol  # 🔥 Modifica esto para obtener el ID del técnico real
                actualizar_falla(id_falla, nuevo_estado, id_tecnico)
                
                messagebox.showinfo("SpiderNet", f"Estado actualizado a '{nuevo_estado_texto}'")
                detallesWindow.destroy()

            CTkButton(detallesWindow, text="Actualizar Estado", fg_color="green", command=lambda:actualizar_estado(rol)).pack(pady=10)

            return

    messagebox.showerror("SpiderNet", "No se encontraron detalles para esta falla.")

def insertarElementos(tablaFallas):
    fallas_registradas = listar_fallas()

    for item in tablaFallas.get_children():
        tablaFallas.delete(item)

    for fallas_almacenadas in fallas_registradas:
        tablaFallas.insert("", END, values=fallas_almacenadas)

def eviar_eliminacion(tablaFallas):
    seleccion = tablaFallas.selection()

    if not seleccion:
        messagebox.showerror("SpiderNet", "Para poder eliminar una falla, seleccionala primero")
        return
    
    identificador = tablaFallas.item(seleccion, "values")[0]
    
    if eliminar_falla(id=identificador):
        messagebox.showinfo("SpiderNet", "La falla fue eliminada de manera exitosa")
        insertarElementos(tablaFallas)
    else:
        messagebox.showinfo("SpiderNet", "No logramos eliminar la falla")

def tabla(fallaWindows, rol):
    contenedorTabla = CTkFrame(fallaWindows, border_color=colores["marcos"], border_width=2,
                            corner_radius=0, fg_color=colores["fondo"])
    
    tablaFallas = ttk.Treeview(contenedorTabla, columns=("Id falla", "Cliente", "Tipo falla", "Estado"), show="headings")
    tablaFallas.heading("Id falla", text="Id falla")
    tablaFallas.heading("Cliente", text="Cliente")
    tablaFallas.heading("Tipo falla", text="Tipo falla")
    tablaFallas.heading("Estado", text="Estado")

    contenedorTabla.place(relx=0.2, rely=0.0, relwidth=0.8, relheight=1.0)
    insertarElementos(tablaFallas)
    tablaFallas.pack(expand=True, fill="both")

    # Crear menú contextual
    menu = Menu(tablaFallas, tearoff=0)
    menu.add_command(label="Eliminar", command=lambda: eviar_eliminacion(tablaFallas))
    menu.add_command(label="Detalles", command=lambda: mostrar_detalles_falla(tablaFallas, rol))
    menu.add_command(label="Refrescar", command=lambda:insertarElementos(tablaFallas))
    def mostrar_menu(event):
        menu.post(event.x_root, event.y_root)

    tablaFallas.bind("<Button-3>", mostrar_menu)  # Evento clic derecho

def reportar_falla_windows(rol):

    lista_clientes = consultarClientes()
    nombre_clientes = [cliente[1] for cliente in lista_clientes]
    fallas_posibles = ['Sin conexión', 'Intermitencia', 'Baja velocidad', 'Otros']

    fallaWindows = CTkToplevel()
    fallaWindows.title("Reportar Falla")
    fallaWindows.geometry("1280x700")
    fallaWindows.resizable(False, False)

    contenedorDatos = CTkFrame(fallaWindows, border_color=colores["marcos"], border_width=2,
                            corner_radius=0, fg_color=colores["fondo"])

    nombreLabel = CTkLabel(contenedorDatos, text="Selecciona el cliente", font=("Arial", 18, "bold"), text_color="white")
    nombreClientes = CTkComboBox(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=8,
                                values=nombre_clientes, width=240)
    
    erroresLabel = CTkLabel(contenedorDatos, text="Falla reportada", font=("Arial", 18, "bold"), text_color="white")
    erroresEnrey = CTkComboBox(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=8,
                                values=fallas_posibles, width=240)
    
    descripcionEntry = CTkTextbox(contenedorDatos, border_color=colores["marcos"], border_width=2,
                                corner_radius=0, width=400, height=380)
    
    btnRegistrar = CTkButton(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color=colores["boton"], text="Generar reporte", text_color="black",
                            width=320,
                            command=lambda: obtener_datos(descripcionEntry, nombreClientes, erroresEnrey, fallaWindows))
    
    btnFallas = CTkButton(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Fallas Resueltas", text_color="black",
                        width=320,
                        command=moduloFallasResueltas)
    
    contenedorDatos.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    nombreLabel.pack(padx=10, pady=10)
    nombreClientes.pack(padx=10, pady=10)
    erroresLabel.pack(padx=10, pady=10)
    erroresEnrey.pack(padx=10, pady=10)
    descripcionEntry.pack(padx=10, pady=10)
    btnRegistrar.pack(padx=10, pady=10)
    btnFallas.pack(padx=10, pady=10)
    tabla(fallaWindows, rol)

    fallaWindows.mainloop()

def reportar_falla_windows_cliente(nombre_cliente, rol):
    fallas_posibles = ['Sin conexión', 'Intermitencia', 'Baja velocidad', 'Otros']

    fallaWindows = CTkToplevel()
    fallaWindows.title("Reportar Falla")
    fallaWindows.geometry("1280x700")
    fallaWindows.resizable(False, False)

    contenedorDatos = CTkFrame(fallaWindows, border_color=colores["marcos"], border_width=2,
                            corner_radius=0, fg_color=colores["fondo"])

    nombreLabel = CTkLabel(contenedorDatos, text="Selecciona el cliente", font=("Arial", 18, "bold"), text_color="white")
    nombreClientes = CTkEntry(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=8,
                                width=240)
    
    erroresLabel = CTkLabel(contenedorDatos, text="Falla reportada", font=("Arial", 18, "bold"), text_color="white")
    erroresEnrey = CTkComboBox(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=8,
                                values=fallas_posibles, width=240)
    
    descripcionEntry = CTkTextbox(contenedorDatos, border_color=colores["marcos"], border_width=2,
                                corner_radius=0, width=400, height=380)
    
    btnRegistrar = CTkButton(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color=colores["boton"], text="Generar reporte", text_color="black",
                            width=320,
                            command=lambda: obtener_datos(descripcionEntry, nombreClientes, erroresEnrey, fallaWindows))
    
    btnFallas = CTkButton(contenedorDatos, border_color=colores["marcos"], border_width=2, corner_radius=6,
                        fg_color=colores["boton"], text="Fallas Resueltas", text_color="black",
                        width=320,
                        command=moduloFallasResueltas)
    
    contenedorDatos.place(relx=0.0, rely=0.0, relwidth=0.2, relheight=1.0)
    nombreLabel.pack(padx=10, pady=10)
    nombreClientes.pack(padx=10, pady=10)
    erroresLabel.pack(padx=10, pady=10)
    erroresEnrey.pack(padx=10, pady=10)
    descripcionEntry.pack(padx=10, pady=10)
    btnRegistrar.pack(padx=10, pady=10)
    btnFallas.pack(padx=10, pady=10)

    nombreClientes.insert(0, nombre_cliente)
    tabla(fallaWindows, rol)

    fallaWindows.mainloop()