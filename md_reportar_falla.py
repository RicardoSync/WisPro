from customtkinter import CTkToplevel, CTkComboBox, CTkLabel, CTkFrame, CTkTextbox, CTkButton
from tkinter import messagebox
from bk_consultas import consultar_nombre_cliente
from bk_insert import insertarFalla

from bk_consultas import consultarClientes
from bk_recursos import colores_ui
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


def reportar_falla_windows():
    # Consultar paquetes cada vez que se abre la ventana
    lista_clientes = consultarClientes()
    nombre_clientes = [cliente[1] for cliente in lista_clientes]  # Extraer solo los nombres de los paquetes
    fallas_posibles = ['Sin conexión','Intermitencia','Baja velocidad','Otros']

    fallaWindows = CTkToplevel()
    fallaWindows.title("Reportar Falla")
    fallaWindows.geometry("500x700")
    fallaWindows._set_appearance_mode("dark")

    contenedorDatos = CTkFrame(fallaWindows, border_color=colores["marcos"], border_width=2,
                            corner_radius=0, fg_color=colores["fondo"])
    
    nombreLabel = CTkLabel(contenedorDatos, text="Selecciona el cliente", font=("Arial", 18, "bold"),
                        text_color="white")
    
    nombreClientes = CTkComboBox(contenedorDatos, border_color=colores["marcos"], border_width=2,
                                corner_radius=8, values=nombre_clientes,
                                width=240)
    
    erroresLabel = CTkLabel(contenedorDatos, text="Falla reportada", font=("Arial", 18, "bold"),
                        text_color="white")
    
    erroresEnrey = CTkComboBox(contenedorDatos, border_color=colores["marcos"], border_width=2,
                                corner_radius=8, values=fallas_posibles,
                                width=240)
    
    descripcionEntry = CTkTextbox(fallaWindows, border_color=colores["marcos"], border_width=2,
                                corner_radius=0)
    
    btnRegistrar = CTkButton(fallaWindows, border_color=colores["marcos"], border_width=2, corner_radius=6,
                            fg_color=colores["boton"], text="Generar reporte", text_color="black",
                            width=320,
                            command=lambda:obtener_datos(descripcionEntry, nombreClientes, erroresEnrey, fallaWindows))
    
    #posicion elementos
    contenedorDatos.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.2)
    nombreLabel.grid(column=0, row=0, padx=10, pady=10)
    nombreClientes.grid(column=1, row=0, padx=10, pady=10)
    erroresLabel.grid(column=0, row=1, padx=10, pady=10)
    erroresEnrey.grid(column=1, row=1, padx=10, pady=10)
    descripcionEntry.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.8)
    btnRegistrar.place(relx=0.2, rely=0.8)
    fallaWindows.mainloop()