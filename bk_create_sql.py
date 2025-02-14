import mysql.connector

"""Este script lo que hace es crear la base de datos con el nombre generado
Y despues insertar el usuario y contraseña con los datos ingresados
"""

def crear_base_datos(nombre, usuario, password, nombre_bd):
    # Crear la consulta para crear la base de datos
    sql_create_db = f"CREATE DATABASE IF NOT EXISTS {nombre_bd};"
    sql_use_db = f"USE {nombre_bd};"
    
    # Script para crear las tablas
    sql_script = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        usuario VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        rol TINYINT NOT NULL CHECK (rol IN (0,1,2))
    );

    CREATE TABLE IF NOT EXISTS paquetes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        velocidad VARCHAR(50) NOT NULL,
        precio DECIMAL(10,2) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        telefono VARCHAR(20),
        email VARCHAR(100),
        direccion TEXT NOT NULL,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
        id_paquete INT,
        ip_cliente VARCHAR(100),
        dia_corte INT,
        estado ENUM("Activo", "Bloqueado", "Suspendido", "Cancelado") NOT NULL,
        FOREIGN KEY (id_paquete) REFERENCES paquetes(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS equipos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        tipo ENUM('Router', 'Antena', 'ONU', 'Otro') NOT NULL,
        marca VARCHAR(50),
        modelo VARCHAR(50),
        mac VARCHAR(50) UNIQUE,
        serial VARCHAR(50) UNIQUE,
        estado ENUM('Rentado', 'Vendido', 'Propio', 'Almacenado') NOT NULL,
        id_cliente INT,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS pagos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT NOT NULL,
        nombre VARCHAR(255),
        monto DECIMAL(10,2) NOT NULL,
        fecha_pago DATETIME DEFAULT CURRENT_TIMESTAMP,
        metodo_pago ENUM('Efectivo', 'Transferencia', 'Tarjeta') NOT NULL,
        cantidad INT NOT NULL,
        cambio INT NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS fallas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT NOT NULL,
        tipo_falla ENUM('Sin conexión', 'Intermitencia', 'Baja velocidad', 'Otros') NOT NULL,
        descripcion TEXT NOT NULL,
        estado TINYINT NOT NULL DEFAULT 0 CHECK (estado IN (0,1,2)),
        fecha_reporte DATETIME DEFAULT CURRENT_TIMESTAMP,
        fecha_reparacion DATETIME NULL,
        id_tecnico INT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE,
        FOREIGN KEY (id_tecnico) REFERENCES usuarios(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS tickets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT NOT NULL,
        categoria ENUM('Soporte técnico', 'Facturación', 'Instalación', 'Otro') NOT NULL,
        descripcion TEXT NOT NULL,
        estado ENUM('Pendiente', 'En proceso', 'Resuelto', 'Cerrado') DEFAULT 'Pendiente',
        fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
        fecha_cierre DATETIME NULL,
        id_responsable INT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE,
        FOREIGN KEY (id_responsable) REFERENCES usuarios(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS credenciales_microtik (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        ip VARCHAR(100),
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100)
    );
    """

    # Insertar el usuario inicial
    sql_insert_usuario = f"""
    INSERT INTO usuarios (nombre, usuario, password, rol) VALUES ("{nombre}", "{usuario}", "{password}", 0);
    """

    try:
        # Conectar a MySQL para crear la base de datos
        connection = mysql.connector.connect(
            host="200.234.227.222",
            user="cisco",
            password="MinuzaFea265/",
            port=3389
        )

        if connection.is_connected():
            print(f"✅ Conexión exitosa al servidor MySQL")
            cursor = connection.cursor()

            # Crear la base de datos
            cursor.execute(sql_create_db)
            connection.commit()  # Commit después de crear la base de datos
            
            # Seleccionar la base de datos creada
            cursor.execute(sql_use_db)
            connection.commit()  # Commit después de usar la base de datos

            # Ejecutar el script para crear las tablas
            for statement in sql_script.split(";"):
                if statement.strip():
                    cursor.execute(statement)
            
            # Insertar el usuario
            cursor.execute(sql_insert_usuario)
            connection.commit()  # Commit después de la inserción

            print(f"✅ Base de datos '{nombre_bd}' creada y tablas configuradas.")
            return True

    except Exception as e:
        print(f"❌ Error al conectar o crear la base de datos: {e}")
        return False

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 Conexión cerrada.")
