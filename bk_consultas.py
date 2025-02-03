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
                COALESCE(p.nombre, 'Sin paquete') AS Paquete
            FROM clientes c
            LEFT JOIN paquetes p ON c.id_paquete = p.id;
        """
        cursor.execute(sql)
        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos

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
            messagebox.showerror("SpiderNet", "No se encontró equipos asignados a este cliente")
            return False
        
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

def consultarEquiposSinCliente():
    """Consulta todos los equipos que no tienen cliente asignado (id_cliente es NULL)."""
    conexion = conexionDB()
    cursor = conexion.cursor()
    query = "SELECT * FROM equipos WHERE id_cliente IS NULL"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

def consultar_equipo_tipo(tipo_equipo):
    conexion = conexionDB()
    cursor = conexion.cursor()
    query = "SELECT * FROM equipos WHERE tipo = %s AND id_cliente IS NULL"
    valores = (tipo_equipo,)  # Asegurar que sea una tupla
    cursor.execute(query, valores)  # Aquí estaba el error
    equipos_filtrados = cursor.fetchall()
    conexion.close()
    return equipos_filtrados

def consutarEquiposActualizacion(id):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "SELECT nombre, tipo, marca, modelo, mac, serial, estado, id_cliente FROM equipos WHERE id =%s"
        valores = (id,)
        cursor.execute(sql, valores)

        equiposDatos = cursor.fetchone()
        cursor.close()
        conexion.close()

        return equiposDatos
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No logramos obtener nada")

def listar_fallas():
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """
            SELECT f.id, c.nombre, f.tipo_falla,  f.estado
            FROM fallas f
            INNER JOIN clientes c ON f.id_cliente = c.id
            WHERE f.estado IN (0,1);
        """
        cursor.execute(sql)
        fallas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return fallas
    except Exception as e:
        print(f"❌ Error al consultar las fallas: {e}")
        return []

def listar_fallas_resueltas():
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """
        SELECT 
            c.id AS id_cliente,
            c.nombre AS nombre_cliente,
            f.tipo_falla,
            f.descripcion,
            f.estado,
            f.fecha_reporte,
            f.fecha_reparacion,
            t.id AS id_usuario,
            t.nombre AS nombre_usuario
        FROM clientes c
        INNER JOIN fallas f ON c.id = f.id_cliente
        INNER JOIN usuarios t ON f.id = t.id;
                
        """
        cursor.execute(sql)
        resueltas = cursor.fetchall()

        cursor.close()
        conexion.close()

        return resueltas
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No logramos obtener las fallas resueltas {err}")
        return []


def detalles_fallas():
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = """
            SELECT f.id, c.nombre, f.tipo_falla, f.descripcion, f.estado, f.fecha_reporte
            FROM fallas f
            INNER JOIN clientes c ON f.id_cliente = c.id
            WHERE f.estado IN (0,1);
        """
        cursor.execute(sql)
        fallas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return fallas
    except Exception as e:
        print(f"❌ Error al consultar las fallas: {e}")
        return []

def consultar_nombre_cliente(nombre):
    try:
        conexion = conexionDB()
        cursor = conexion.cursor()
        sql = "SELECT id FROM clientes WHERE nombre = %s"
        valores = (nombre, )
        cursor.execute(sql, valores)
        nombre_cliente = cursor.fetchone()

        if not nombre_cliente:
            messagebox.showerror("SpiderNet", "No logramos cargar ningun cliente")
            return False
        
        conexion.close()
        cursor.close()

        return nombre_cliente
    
    except Exception as err:
        messagebox.showerror("SpiderNet", f"No logramos consultar a los clientes {err}")