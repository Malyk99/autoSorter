import os
import shutil
import datetime
import json

# Leer configuración desde config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

origen = config["origen"]
log_path = config["log"]
destinos = config["destinos"]

# Extensiones agrupadas por tipo
tipos = {
    'pdf': ['.pdf'],
    'imagenes': ['.jpg', '.jpeg', '.gif', '.bmp', '.webp'],
    'pngs': ['.png'],
    'zip': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'documentos': ['.txt', '.doc', '.docx', '.odt'],
    'excel': ['.xls', '.xlsx', '.ods'],
    'videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv']
}

# Crear carpetas de destino si no existen
for ruta in destinos.values():
    os.makedirs(ruta, exist_ok=True)

# Función para log
def log(mensaje):
    with open(log_path, 'a', encoding='utf-8') as f:
        hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'[{hora}] {mensaje}\n')

# Función para obtener tipo por extensión
def obtener_tipo(ext):
    for tipo, extensiones in tipos.items():
        if ext.lower() in extensiones:
            return tipo
    return 'otros'

# Extensiones a ignorar (descargas incompletas)
extensiones_ignoradas = ['.crdownload', '.part', '.tmp']

# Recorrer los archivos en la carpeta de descargas
for archivo in os.listdir(origen):
    ruta_archivo = os.path.join(origen, archivo)
    if os.path.isfile(ruta_archivo):
        _, extension = os.path.splitext(archivo)

        if extension.lower() in extensiones_ignoradas:
            log(f'Ignorado (incompleto): {archivo}')
            continue

        tipo = obtener_tipo(extension)
        carpeta_destino = destinos.get(tipo, destinos['otros'])

        # Evitar sobrescribir: renombrar si ya existe
        nombre_base, ext = os.path.splitext(archivo)
        nuevo_nombre = archivo
        contador = 1
        ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)

        while os.path.exists(ruta_destino):
            nuevo_nombre = f"{nombre_base} ({contador}){ext}"
            ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
            contador += 1

        shutil.move(ruta_archivo, ruta_destino)
        log(f'Movido: {archivo} → {ruta_destino}')
