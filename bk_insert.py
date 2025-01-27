from bk_connect import conexionDB
from tkinter import messagebox
from bk_consultas import consultarPaqueteID

def insertarUsuarios(nombre, username, password, rol):
    try:
        tipo_usuario = None

        if rol == "Admin":
            tipo_usuario = 0
        elif rol == "Tecnico":
            tipo_usuario = 1
        elif rol == "Cajero":
            tipo_usuario = 2
        
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO usuarios (nombre, usuario, password, rol) VALUES (%s,%s,%s,%s)"
        valores = (nombre, username, password, tipo_usuario)
        cursor.execute(sql, valores)

        conexion.commit()
        conexion.close()
        cursor.close()

        return 0
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos insertar el usuario {err}")


def insertarPaquete(nombre, velocidad, precio):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO paquetes (nombre, velocidad, precio) VALUES (%s,%s,%s)"
        valores = (nombre, velocidad, precio)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return 0
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos insertar el paquete debido a {err}")

def insertarCliente(nombre, telefono, email, direccion, paquete):
    idPaquete = consultarPaqueteID(paquete)

    if not idPaquete:
        messagebox.showerror("SpiderNet", "No logramos encontrar ese paquete, intenta una vex mas")
        return
    
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO clientes (nombre, telefono, email, direccion, id_paquete) VALUES (%s,%s,%s,%s,%s)"
        valores = (nombre, telefono, email, direccion, idPaquete)
        cursor.execute(sql, valores)

        conexion.commit()
        conexion.close()
        cursor.close()

        messagebox.showinfo("SpiderNet", f"El cliente {nombre} se registro con exito")
        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos almacenar al cliente {err}")