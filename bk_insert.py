from bk_connect import conexionDB
from tkinter import messagebox
from bk_consultas import consultarPaqueteID
from bk_generar_pago import generar_recibo
import mysql.connector

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

def insertarCliente(nombre, telefono, email, direccion, paquete, ip_cliente, dia_corte):
    idPaquete = consultarPaqueteID(paquete)
    if not idPaquete:
        messagebox.showerror("SpiderNet", "No logramos encontrar ese paquete, intenta una vex mas")
        return
    
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        estado = "Activo"
        sql = "INSERT INTO clientes (nombre, telefono, email, direccion, id_paquete, ip_cliente, dia_corte, estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        valores = (nombre, telefono, email, direccion, idPaquete, ip_cliente, dia_corte, estado)
        cursor.execute(sql, valores)

        conexion.commit()
        conexion.close()
        cursor.close()

        messagebox.showinfo("SpiderNet", f"El cliente {nombre} se registro con exito")
        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos almacenar al cliente {err}")

def insertarPago(id_cliente, monto, metodo_pago, cantidad, cambio, nombre_cliente, paquete, nombre_admin):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO pagos (id_cliente, nombre, monto, metodo_pago, cantidad, cambio) VALUES (%s,%s,%s,%s,%s,%s)"
        valores = (id_cliente, nombre_cliente, monto, metodo_pago, cantidad, cambio)
        cursor.execute(sql, valores)

        conexion.commit()
        conexion.close()
        cursor.close()
        generar_recibo(id_cliente, nombre_cliente, paquete, monto, metodo_pago, cantidad, cambio, nombre_admin)
        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos registrar el pago {err}")

def insertarEquipo(nombre, tipo, marca, modelo, mac, serial, estado, id_cliente):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO equipos (nombre, tipo, marca, modelo, mac, serial, estado, id_cliente) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        valores = (nombre, tipo, marca, modelo, mac, serial, estado, id_cliente)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos asigar el equipo, error {err}")

def insertarEquipo_solo(nombre, tipo, marca, modelo, mac, serial, estado):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO equipos (nombre, tipo, marca, modelo, mac, serial, estado) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        valores = (nombre, tipo, marca, modelo, mac, serial, estado)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos asigar el equipo, error {err}")

def insertarFalla(id_cliente, tipo_falla, descripcion, estado):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO fallas (id_cliente, tipo_falla, descripcion, estado) VALUES (%s,%s,%s,%s)"
        valores = (id_cliente, tipo_falla, descripcion, estado)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        return True
    
    except mysql.connector.Error as err:
        #messagebox.showerror("SpiderNet", f"No logramos generar el reporte de falla {err}")
        print(f"{err}")
        return False

def insertar_microtik(nombre, username, password, ip):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "INSERT INTO credenciales_microtik(nombre, ip, username, password) VALUES (%s,%s,%s,%s)"
        valores = (nombre, ip, username, password)
        cursor.execute(sql, valores)

        conexion.commit()
        
        cursor.close()
        conexion.close()

        return True
    
    except Exception as err:
        print(f"Error {err}")
        return False