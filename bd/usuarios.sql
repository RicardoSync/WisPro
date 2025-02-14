CREATE DATABASE spider_user;
USE spider_user;

-- Tabla de clientes
CREATE TABLE usuarios_spider (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_isp VARCHAR(100) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    nombre_db VARCHAR(100) NOT NULL
);
