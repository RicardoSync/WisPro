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