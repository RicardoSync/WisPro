from bk_connect import conexionDB
from tkinter import messagebox
from bk_consultas import consultarPaqueteID

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

def actualizarPaquete(id, nombre, velocidad, precio):
    try:
        daniela = conexionDB()
        cursor = daniela.cursor()
        sql = """UPDATE paquetes 
            SET nombre = %s, velocidad = %s, precio = %s
            WHERE id = %s"""
        valores = (nombre, velocidad, precio, id)
        cursor.execute(sql, valores)

        daniela.commit()
        cursor.close()
        daniela.close()

        return 0
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos actualizar el paquete {nombre} por problemas {err}")

def actualizacion_cliente(id, nombre, telefono, email, direccion, nombre_paquete):
    try:
        if not nombre_paquete:
            messagebox.showerror("SpiderNet", "No podemos almacenar un paquete vacio")
            return
        
        id_paquete = consultarPaqueteID(nombre_paquete)

        if not id_paquete:
            messagebox.showerror("SpiderNet", f"No se encontró el paquete '{nombre_paquete}'")
            return False

        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """UPDATE clientes
            SET nombre = %s, telefono = %s, email = %s, direccion = %s, id_paquete = %s
            WHERE id = %s"""
        valores = (nombre, telefono, email, direccion, id_paquete, id)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        messagebox.showinfo("SpiderNet", "Cliente actualizado")
        return True


    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos actualizar al cliente {nombre}. Error: {err}")

def actualizacion_equipo(nombre, tipo, marca, modelo, mac, serial, estado, id_equipo):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """UPDATE equipos
            SET nombre = %s, tipo = %s, marca = %s, modelo = %s, mac = %s, serial = %s, estado = %s
            WHERE id = %s"""
        valores = (nombre, tipo, marca, modelo, mac, serial, estado, id_equipo)
        
        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()
        
        return True

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos actualizar el equipo: {err}")
        return False

def actualizar_asignacion(id_equipo, id_cliente):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """UPDATE equipos
            SET id_cliente = %s
            WHERE id = %s"""
        
        valores = (id_cliente, id_equipo)
        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()
        
        return True

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos actualizar el equipo: {err}")
        return False

def elimnar_equipo_de_cliente(id_equipo):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """UPDATE equipos
            SET id_cliente = NULL
            WHERE id = %s"""
        cursor.execute(sql, (id_equipo,))
        conexion.commit()

        cursor.close()
        conexion.close()
        
        return True

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos actualizar el equipo: {err}")
        return False

def actualizar_microtik(id, username, password, ip, nombre):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """UPDATE credenciales_microtik
        SET nombre = %s, ip = %s, username = %s, password = %s WHERE id = %s"""
        valores = (nombre, ip, username, password, id)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    except Exception as err:
        print(f"No podemos actualizar {err}")
        return False

def actualizar_falla(id_falla, nuevo_estado, id_tecnico):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """
            UPDATE fallas 
            SET estado = %s, fecha_reparacion = NOW(), id_tecnico = %s 
            WHERE id = %s;
        """
        cursor.execute(sql, (nuevo_estado, id_tecnico, id_falla))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("✅ Falla actualizada correctamente.")
    except Exception as e:
        print(f"❌ Error al actualizar la falla: {e}")

def actualizar_bloqueo(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """
        UPDATE clientes
        SET estado = "Bloqueado" WHERE id = %s"""
        cursor.execute(sql, (id, ))
        conexion.commit()

        cursor.close()
        conexion.close()

        return True
    
    except Exception as err:
        print(f"No podemos actualizar el bloque del cliente {err} en base de datos")
        return False
    

def actualizar_desbloqueo(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """
        UPDATE clientes
        SET estado = "Activo" WHERE id = %s"""
        cursor.execute(sql, (id, ))
        conexion.commit()

        cursor.close()
        conexion.close()

        return True
    
    except Exception as err:
        print(f"No podemos actualizar el bloque del cliente {err} en base de datos")
        return False