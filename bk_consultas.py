from bk_connect import conexionDB
from tkinter import messagebox

def consultaUsuarios():
    try:
        conn = conexionDB()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, usuario, password, rol FROM usuarios")
        usuarios = cursor.fetchall()

        cursor.close()
        conn.close()

        return usuarios
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos realizar la consulta de los usuarios {err}")

def consultarPaquetes():
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, velocidad, precio FROM paquetes")
        paquetes = cursor.fetchall()

        cursor.close()
        conexion.close()

        return paquetes
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos realizar la consulta de los paquetes {err}")