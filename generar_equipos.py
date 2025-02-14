import mysql.connector
import random
from bk_connect import conexionDB

def generar_equipos(numero_equipos):
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

    try:
        # Conectar a la base de datos
        conn = conexionDB()
        cursor = conn.cursor()
        
        # Query SQL para inserción
        sql = """
        INSERT INTO equipos (nombre, tipo, marca, modelo, mac, serial, estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Lista para almacenar los valores a insertar en lotes
        datos_insertar = []
        
        for _ in range(50):  # Generar 30,000 equipos
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
            serial = f"SN{random.randint(1000000, 9999999)}"  # Serial más largo
            estado = random.choice(estados)

            datos_insertar.append((f"{tipo} {marca}", tipo, marca, modelo, mac, serial, estado))

            # Insertar en lotes de 1000 para mayor eficiencia
            if len(datos_insertar) >= numero_equipos:
                cursor.executemany(sql, datos_insertar)
                conn.commit()
                datos_insertar = []  # Limpiar lista

        # Insertar cualquier dato restante
        if datos_insertar:
            cursor.executemany(sql, datos_insertar)
            conn.commit()

        return True

    except mysql.connector.Error as e:
        print("Error al conectar a MySQL:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
