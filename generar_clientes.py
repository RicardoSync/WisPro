import customtkinter as ctk
from bk_connect import conexionDB
import mysql.connector
import random
import faker
from generar_equipos import generar_equipos

def generar_clientes(numero_clientes):
    fake = faker.Faker()
    try:
        conn = conexionDB()
        cursor = conn.cursor()
        sql = """
        INSERT INTO clientes (nombre, telefono, email, direccion, id_paquete, ip_cliente, dia_corte, estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        datos_insertar = []
        
        for _ in range(numero_clientes):
            nombre = fake.name()
            telefono = f"{random.randint(1000000000, 6999999999)}"
            email = nombre.lower().replace(" ", ".") + "@doblenet.com"
            direccion = fake.address().replace("\n", ", ")
            id_paquete = None
            ip_cliente = f"192.168.1.{random.randint(2, 254)}"
            dia_corte = random.randint(1, 30)
            estado = "Activo"

            datos_insertar.append((nombre, telefono, email, direccion, id_paquete, ip_cliente, dia_corte, estado))
            
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

def md_generacion():
    ventana = ctk.CTkToplevel()
    ventana.title("Generación")
    ventana.geometry("400x250")

    ctk.CTkLabel(ventana, text="Ingresa la cantidad de clientes que quieres generar:").pack(pady=5)
    entry_clientes = ctk.CTkEntry(ventana)
    entry_clientes.pack(pady=5)
    
    ctk.CTkLabel(ventana, text="Ingresa la cantidad de equipos a generar:").pack(pady=5)
    entry_equipos = ctk.CTkEntry(ventana)
    entry_equipos.pack(pady=5)
    
    def ejecutar_generacion():
        try:
            num_clientes = int(entry_clientes.get())
            numero_equipos = int(entry_equipos.get()) 
            generar_clientes(num_clientes)
            generar_equipos(numero_equipos)
            ctk.CTkLabel(ventana, text="Clientes generados exitosamente!").pack(pady=5)
        except ValueError:
            ctk.CTkLabel(ventana, text="Ingrese un número válido").pack(pady=5)
    
    btn_generar = ctk.CTkButton(ventana, text="Generar", command=ejecutar_generacion)
    btn_generar.pack(pady=10)
    
    ventana.mainloop()