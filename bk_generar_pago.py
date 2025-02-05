import os
import platform
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def generar_recibo(id_cliente, nombre_cliente, paquete, monto, metodo_pago, cantidad, cambio, nombre_admin):
    width, height = 400, 600  # Tamaño más parecido a un recibo térmico
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    
    try:
        font = ImageFont.truetype("arial.ttf", 18)
        bold_font = ImageFont.truetype("arialbd.ttf", 20)
        small_font = ImageFont.truetype("arial.ttf", 14)
    except IOError:
        font = ImageFont.load_default()
        bold_font = font
        small_font = font
    
    draw.text((100, 20), "SPIDERNET", font=bold_font, fill="black")
    draw.text((120, 50), "Recibo de Pago", font=font, fill="black")
    draw.line((20, 80, width - 20, 80), fill="black", width=2)
    
    draw.text((20, 100), f"Fecha: {fecha_actual}", font=small_font, fill="black")
    draw.text((20, 130), f"Cliente: {nombre_cliente}", font=small_font, fill="black")
    draw.text((20, 160), f"Paquete: {paquete}", font=small_font, fill="black")
    
    draw.line((20, 190, width - 20, 190), fill="black", width=1)
    draw.text((20, 210), f"Monto: ${monto:.2f}", font=font, fill="black")
    draw.text((20, 240), f"Método de Pago: {metodo_pago}", font=font, fill="black")
    draw.text((20, 270), f"Cantidad Entregada: ${cantidad:.2f}", font=font, fill="black")
    draw.text((20, 300), f"Cambio: ${cambio:.2f}", font=font, fill="black")
    draw.text((20, 330), f"Le atendio el usuario: {nombre_admin}", font=font, fill="black")
    draw.line((20, 190, width - 20, 190), fill="black", width=1)

    draw.text((100, 360), "¡Gracias por su pago!", font=small_font, fill="black")
    
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