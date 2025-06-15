import os
import shutil

# Ruta de origen (Descargas)
origen = r'C:\Users\Malyk\Downloads'

# Diccionario de carpetas destino por tipo de archivo
destinos = {
    'pdf': r'C:\Users\Malyk\Documents\PDFs',
    'imagenes': r'C:\Users\Malyk\Pictures\AutoSorted\Images',
    'pngs': r'C:\Users\Malyk\Pictures\AutoSorted\PNGs',
    'zip': r'C:\Users\Malyk\Documents\Compressed',
    'documentos': r'C:\Users\Malyk\Documents\TextFiles',
    'excel': r'C:\Users\Malyk\Documents\ExcelFiles',
    'videos': r'C:\Users\Malyk\Videos\AutoSorted',
    'otros': r'C:\Users\Malyk\Documents\Otros'
}

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

# Función para obtener tipo por extensión
def obtener_tipo(ext):
    for tipo, extensiones in tipos.items():
        if ext.lower() in extensiones:
            return tipo
    return 'otros'

# Recorrer los archivos en la carpeta de descargas
for archivo in os.listdir(origen):
    ruta_archivo = os.path.join(origen, archivo)
    if os.path.isfile(ruta_archivo):
        _, extension = os.path.splitext(archivo)
        tipo = obtener_tipo(extension)
        ruta_destino = os.path.join(destinos[tipo], archivo)
        
        # Evitar sobrescribir archivos con el mismo nombre
        if not os.path.exists(ruta_destino):
            shutil.move(ruta_archivo, ruta_destino)
            print(f'Movido: {archivo} → {destinos[tipo]}')
        else:
            print(f'Ya existe en destino: {archivo}')
