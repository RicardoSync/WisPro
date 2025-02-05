from bk_connect import conexionDB
from tkinter import messagebox

def eliminarUsuario(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "DELETE FROM usuarios WHERE id = %s"
        valores = (id, )
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("SpiderNet", "Usuario eliminado de manera exitosa")
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos eliminar a ese usuario {err}")

def eliminarPaquete(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "DELETE FROM paquetes WHERE id = %s"
        valores = (id, )
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("SpiderNet", "Usuario eliminado de manera exitosa")
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos eliminar a ese usuario {err}")

def eliminarCliente(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        valores = (id, )
        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        messagebox.showinfo("SpiderNet", "El cliente fue eliminado")
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos eliminar al cliente {err}")

def eliminarEquipo(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "DELETE FROM equipos WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("SpiderNet", "Equipo eliminado")
        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos eliminar el equipo por error {err}")

def eliminar_falla(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "DELETE FROM fallas WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos eliminar la falla por error {err}")

def eliminar_microtik(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "DELETE FROM credenciales_microtik WHERE id = %s"
        valores = (id, )
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    
    except Exception as err:
        print("error tipo {err}")
        return False