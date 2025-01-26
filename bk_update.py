from bk_connect import conexionDB
from tkinter import messagebox

def actualizarUsuario(id, nombre, usuario, password, rol):
    try:
        tipo_usuario = None

        if rol == "Admin":
            tipo_usuario = 0
        elif rol == "Tecnico":
            tipo_usuario = 1
        elif rol == "Cajero":
            tipo_usuario = 2
        else:
            tipo_usuario = 00
        

        conexion = conexionDB()
        cursor = conexion.cursor()

        sql = """UPDATE usuarios 
                SET nombre = %s, usuario = %s, password = %s, rol = %s 
                WHERE id = %s"""
        
        valores = (nombre, usuario, password, tipo_usuario, id)  # CORRECCIÓN AQUÍ
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()  # Asegurar que se cierra la conexión correctamente

        return "Exito"

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos actualizar al usuario {usuario}, tipo de error {err}")