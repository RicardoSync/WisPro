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

def consultarPaqueteID(nombrePaquete):
    try:
        daniela = conexionDB()
        cursor = daniela.cursor()
        sql = "SELECT id FROM paquetes WHERE nombre = %s"
        valores = (nombrePaquete, )
        cursor.execute(sql, valores)

        idPaquete = cursor.fetchone()
        cursor.close()
        daniela.close()

        return idPaquete[0] if idPaquete else None  # Retorna el ID o None
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos buscar el paquete con nombre {nombrePaquete} por error {err}")
        return None

def consultarClientes():

    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """
            SELECT 
                c.id, 
                c.nombre, 
                c.telefono, 
                c.email,
                c.direccion, 
                c.fecha_registro, 
                p.nombre AS Paquete
            FROM clientes c
            INNER JOIN paquetes p ON c.id_paquete = p.id;
        """
        cursor.execute(sql)
        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        # Verificar si hay datos antes de devolverlos
        if datos:
            return datos
        else:
            messagebox.showinfo("SpiderNet", "No se encontró el cliente con ID = 1")
            return None
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos consultar al cliente. Error: {err}")
        return None

def consultarPaqueteNombre(nombrePaquete):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "SELECT precio FROM paquetes WHERE nombre = %s"
        valores = (nombrePaquete,)
        cursor.execute(sql, valores)
        precioPaquete = cursor.fetchone()

        cursor.close()
        conexion.close()

        if not precioPaquete:
            messagebox.showerror("SpiderNet", "NO logramos obtener el precio del paquete")
            return "Desconocido"
        
        return precioPaquete
    
    except Exception as err:
        messagebox.showerror("SpiderNet", "No logramos encontrar este paquete")

def consultarPagos():
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_cliente, nombre, monto, fecha_pago, metodo_pago FROM pagos")
        
        pagos = cursor.fetchall()
        conexion.close()  # Cerrar la conexión antes de retornar

        if not pagos:
            messagebox.showerror("SpiderNet", "No logramos obtener los pagos de la base de datos")
            return []
        
        return pagos
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No logramos cargar los pagos: {err}")
        return []

def consultarPagoNombre(nombreCliente):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "SELECT id_cliente, nombre, monto, fecha_pago, metodo_pago FROM pagos WHERE nombre LIKE %s"
        valores = (f"%{nombreCliente}%",)  # Permitir búsqueda parcial con LIKE
        cursor.execute(sql, valores)

        pagosCliente = cursor.fetchall()  # Cambiado de fetchone() a fetchall()
        conexion.close()

        if not pagosCliente:
            messagebox.showerror("SpiderNet", "No podemos encontrar este cliente")
            return []
        
        return pagosCliente

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos conectar: {err}")
        return []

def consultarPagoID(idCliente):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "SELECT id_cliente, nombre, monto, fecha_pago, metodo_pago FROM pagos WHERE id_cliente = %s"
        valores = (idCliente,)
        cursor.execute(sql, valores)

        pagoCliente = cursor.fetchall()
        conexion.close()

        if not pagoCliente:
            messagebox.showerror("SpiderNet", "No se encontró un cliente con este ID")
            return []
        
        return pagoCliente

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos conectar: {err}")
        return []

def consultarEquipos():
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, tipo, marca, modelo, estado, id_cliente FROM equipos")
        
        pagos = cursor.fetchall()
        conexion.close()  # Cerrar la conexión antes de retornar

        if not pagos:
            messagebox.showerror("SpiderNet", "No logramos obtener los pagos de la base de datos")
            return []
        
        return pagos
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No logramos cargar los pagos: {err}")
        return []
    
def consultarEquipoID(idCliente):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "SELECT id, nombre, tipo, marca, modelo, estado, id_cliente FROM equipos WHERE id_cliente = %s"
        valores = (idCliente,)
        cursor.execute(sql, valores)

        pagoCliente = cursor.fetchall()
        conexion.close()

        if not pagoCliente:
            messagebox.showerror("SpiderNet", "No se encontró un cliente con este ID")
            return []
        
        return pagoCliente

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos conectar: {err}")
        return []
    
def consultarEquipoNombre(nombreCliente):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "SELECT id, nombre, tipo, marca, modelo, estado, id_cliente FROM equipos WHERE nombre = %s"
        valores = (f"%{nombreCliente}%",)  # Permitir búsqueda parcial con LIKE
        cursor.execute(sql, valores)

        pagosCliente = cursor.fetchall()  # Cambiado de fetchone() a fetchall()
        conexion.close()

        if not pagosCliente:
            messagebox.showerror("SpiderNet", "No podemos encontrar este cliente")
            return []
        
        return pagosCliente

    except Exception as err:
        messagebox.showerror("SpiderNet", f"No podemos conectar: {err}")
        return []
