import os
import platform
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from tkinter import messagebox
from datetime import datetime

def generar_recibo(id_cliente, nombre_cliente, paquete, monto, metodo_pago, cantidad, cambio):
    width, height = 600, 800
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
        bold_font = ImageFont.truetype("arialbd.ttf", 22)
    except IOError:
        font = ImageFont.load_default()
        bold_font = font
    
    draw.rectangle([(10, 10), (width - 10, height - 10)], outline="black", width=3)
    draw.text((20, 40), "SpiderNet - Recibo de Pago", font=bold_font, fill="black")
    draw.text((20, 80), f"Fecha: {fecha_actual}", font=font, fill="black")
    draw.text((20, 120), f"Cliente: {nombre_cliente}", font=font, fill="black")
    draw.text((20, 160), f"Paquete: {paquete}", font=font, fill="black")
    draw.text((20, 200), f"Monto: ${monto:.2f}", font=font, fill="black")
    draw.text((20, 240), f"Método de Pago: {metodo_pago}", font=font, fill="black")
    draw.text((20, 280), f"Cantidad Entregada: ${cantidad:.2f}", font=font, fill="black")
    draw.text((20, 320), f"Cambio: ${cambio:.2f}", font=font, fill="black")
    draw.line((20, 360, width - 20, 360), fill="black", width=2)
    draw.text((20, 400), "Gracias por su pago!", font=font, fill="black")
    
    watermark_font = ImageFont.truetype("arial.ttf", 50)
    draw.text((width//4, height//2), "SpiderNet", font=watermark_font, fill=(200, 200, 200, 128))
    
    # Guardar la imagen en el escritorio en la carpeta Recibos SpiderNet
    directorio_recibos = Path.home() / "Desktop" / "Recibos SpiderNet"
    directorio_recibos.mkdir(parents=True, exist_ok=True)
    
    ruta_salida = directorio_recibos / f"recibo_cliente_{id_cliente}.png"
    image.save(ruta_salida)
    print(f"Recibo guardado como {ruta_salida}")
    
    # Abrir el archivo automáticamente
    if platform.system() == "Windows":
        os.startfile(ruta_salida)
    elif platform.system() == "Darwin":
        subprocess.run(["open", ruta_salida])
    elif platform.system() == "Linux":
        subprocess.run(["xdg-open", ruta_salida])
