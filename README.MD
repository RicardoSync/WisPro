## 📌 WisPro  

**WisPro** es una aplicación de código abierto desarrollada en Python que permite gestionar datos mediante una interfaz gráfica basada en `customtkinter` y una base de datos MySQL.  

---  

### ✨ Características  
- Interfaz gráfica con `customtkinter`.  
- Conexión a bases de datos MySQL, tanto en local como en la nube.  
- Generación de datos de prueba con `faker`.  
- Soporte para conexión remota mediante `paramiko`.  

---  

## 🚀 Instalación y ejecución  

### 🖥 Requisitos previos  
Antes de ejecutar **WisPro**, asegúrate de tener instalado:  
- **Python 3.x**  
- **Tkinter** (incluido en la mayoría de instalaciones de Python, pero en Linux puede ser necesario instalarlo manualmente).  
- **MySQL** (local o remoto).  

### 🔧 Instalación en Linux  
```bash  
# Instalar Python y Tkinter si no están instalados  
sudo apt update && sudo apt install python3 python3-tk -y  

# Crear y activar un entorno virtual  
python3 -m venv venv  
source venv/bin/activate  

# Instalar las dependencias  
pip install customtkinter pillow mysql-connector-python faker paramiko  
```

### 🖥 Instalación en Windows  
1. Descargar e instalar [Python](https://www.python.org/downloads/) (marcar la opción "Add Python to PATH").  
2. Abrir un terminal (`cmd` o `PowerShell`) y ejecutar:  
   ```powershell  
   python -m venv venv  
   venv\Scripts\activate  
   pip install customtkinter pillow mysql-connector-python faker paramiko  
   ```  

---  

## ⚙️ Configuración de la Base de Datos  
1. En la carpeta `DB`, encontrarás el script para crear la base de datos. Ejecûtalo en MySQL (local o en la nube).  
2. Configura las credenciales en el archivo `config.json`:  
   ```json  
   {  
       "host": "IP_DEL_SERVIDOR",  
       "port": 3306,  
       "user": "USUARIO",  
       "password": "CONTRASEÑA",  
       "database": "NOMBRE_BD"  
   }  
   ```  

---  

## ▶️ Ejecución  
Una vez configurado el entorno y la base de datos, ejecuta el script principal:  
```bash  
python WisPro.py  
```

---  

## 📝 Licencia  
Este software es **open source** y está disponible para su uso, modificación y optimización. **No está permitido su uso con fines de lucro.** Si lo usas o te inspiras en él, recuerda que debe seguir siendo gratuito para todos.  

