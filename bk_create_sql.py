import mysql.connector
from mysql.connector import Error

# Solicitar datos de conexión
host = input("Ingrese la dirección del servidor MySQL (ej. localhost o IP remota): ")
user = input("Ingrese el usuario de MySQL: ")
password = input("Ingrese la contraseña de MySQL: ")
port = input("Ingresa el puerto de conexion MySQL: ")

# Script SQL para crear la base de datos y tablas
sql_script = """
CREATE DATABASE IF NOT EXISTS local_2025;
USE local_2025;

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

INSERT INTO usuarios (nombre, usuario, password, rol) VALUES ("spidernet", "spidernet", "spidernet", 0);

"""

try:
    # Conectar a MySQL
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    
    if connection.is_connected():
        print("✅ Conexión exitosa a MySQL")
        cursor = connection.cursor()
        
        # Ejecutar el script SQL
        for statement in sql_script.split(";"):
            if statement.strip():
                cursor.execute(statement)
        
        print("✅ Base de datos y tablas creadas correctamente.")
    
except Error as e:
    print(f"❌ Error al conectar con MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔌 Conexión cerrada.")
