from mysql.connector import Connect, Error 
from tkinter import messagebox
from bk_create_sql import crear_base_datos
def conexion():
    try:
        conn = Connect(
            host="200.234.227.222",
            port=3389,
            user="cisco",
            password="MinuzaFea265/",
            database="spider_user"
        )
        return conn
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"Tenemos un error de conexión al servidor")


def enviar_datos(username, password, nombreISP, nombre, telefono, email, direccion, nombre_db):
    try:
        server = conexion()
        cursor = server.cursor()
        sql = """INSERT INTO clientes (nombre_isp, nombre, telefono, email, direccion, nombre_db) VALUES
                (%s,%s,%s,%s,%s,%s)"""
        valores = (nombreISP, nombre, telefono, email, direccion, nombre_db)
        cursor.execute(sql, valores)

        server.commit()
        cursor.close()
        server.close()
        if crear_base_datos(nombre, usuario=username, password=password, nombre_bd=nombre_db):
            messagebox.showinfo("SpiderNet", f"Se registro el usuario {username} y se creo su base de datos {nombre_db}.\nAhora puede iniciar sesión en el sistema")
        else:
            messagebox.showerror("SpiderNet", "No logramos crear el usuario ni establecer conexión. Revisa el error desde terminal")

        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"Tenemos un problema al almacenar el nuevo usuario {err}")