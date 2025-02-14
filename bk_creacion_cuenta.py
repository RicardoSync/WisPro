from mysql.connector import Connect, Error 
from tkinter import messagebox
from bk_create_sql import crear_base_datos

def conexion():
    try:
        conn = Connect(
            host="localhost",
            port=3306,
            user="root",
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
        sql = """INSERT INTO usuarios_spider (nombre_isp, nombre, telefono, email, direccion, nombre_db) VALUES
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

def obtener_database(numero):
    try:
        server = conexion()
        cursor = server.cursor()
        cursor.execute("SELECT nombre_db FROM usuarios_spider WHERE telefono = %s", (numero, ))
        
        db_name = cursor.fetchone()

        cursor.close()
        server.close()

        return db_name
    
    except Exception as e:
        print(f"No podemos obtener los datos {e}")
        return False