import mysql.connector
import random

# Configuración de conexión
config = {
    "host": "200.234.227.222",
    "port": 3389,
    "user": "cisco",
    "password": "MinuzaFea265/",
    "database": "pedos"
}

# Listas de datos de ejemplo
tipos_equipos = ["Router", "Antena", "ONU"]
marcas = {
    "Router": ["TP-Link", "Mikrotik", "Cisco"],
    "Antena": ["Ubiquiti", "Cambium", "Mimosa", "LiteBeam"],
    "ONU": ["Huawei", "ZTE", "Nokia"]
}
modelos = {
    "TP-Link": ["Archer C6", "Archer AX50"],
    "Mikrotik": ["hAP ac2", "RB3011"],
    "Cisco": ["RV340", "C1100"],
    "Ubiquiti": ["NanoBeam AC", "PowerBeam 5AC"],
    "Cambium": ["ePMP 1000", "PMP450"],
    "Mimosa": ["C5x", "B5c"],
    "Huawei": ["HG8245H", "EG8145X6"],
    "ZTE": ["F660", "ZXHN F680"],
    "Nokia": ["G-240G-E", "G-140W-C"],
    "LiteBeam": ["M5", "AC", "Nano"]
}
estados = ["Rentado", "Vendido", "Propio"]

# Conectar a la base de datos
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    for cliente_id in range(1, 1200):  # Clientes del ID 13 al 318
        tipo = random.choice(tipos_equipos)
        marca = random.choice(marcas[tipo])
        modelo = random.choice(modelos[marca])
        mac = "00:{:02X}:{:02X}:{:02X}:{:02X}:{:02X}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        serial = f"SN{random.randint(100000, 999999)}"
        estado = random.choice(estados)

        sql = """
        INSERT INTO equipos (nombre, tipo, marca, modelo, mac, serial, estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (f"{tipo} {marca}", tipo, marca, modelo, mac, serial, estado))

    conn.commit()
    print("Equipos registrados exitosamente.")

except mysql.connector.Error as e:
    print("Error al conectar a MySQL:", e)

