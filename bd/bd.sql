-- Crear la base de datos
CREATE DATABASE wisp_control;
USE wisp_control;

-- Tabla de usuarios (para iniciar sesión y roles)
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol TINYINT NOT NULL CHECK (rol IN (0,1,2)) -- 0 = Admin, 1 = Técnico, 2 = Cajero
);

-- Tabla de clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_paquete INT,
    FOREIGN KEY (id_paquete) REFERENCES paquetes(id) ON DELETE SET NULL
);

-- Tabla de paquetes (Internet o servicios contratados)
CREATE TABLE paquetes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    velocidad VARCHAR(50) NOT NULL, -- Ejemplo: "20 Mbps", "50 Mbps"
    precio DECIMAL(10,2) NOT NULL
);

-- Tabla de equipos (Router, ONU, Antenas, etc.)
CREATE TABLE equipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('Router', 'Antena', 'ONU', 'Otro') NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    mac VARCHAR(50) UNIQUE,
    serial VARCHAR(50) UNIQUE,
    estado ENUM('Rentado', 'Vendido', 'Propio') NOT NULL, -- Estado del equipo
    id_cliente INT, -- Cliente al que está asignado (puede ser NULL)
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE SET NULL
);

-- Tabla de pagos (Registro de pagos de los clientes)
CREATE TABLE pagos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha_pago DATETIME DEFAULT CURRENT_TIMESTAMP,
    metodo_pago ENUM('Efectivo', 'Transferencia', 'Tarjeta') NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id) ON DELETE CASCADE
);
