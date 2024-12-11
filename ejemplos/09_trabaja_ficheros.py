# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 09_trabaja_ficheros.py

import os

def crea_ficheros(ruta, nombre, cantidad):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
    for i in range(cantidad):
        archivo_ruta = os.path.join(ruta, f"{nombre}_{i}.txt")
        with open(archivo_ruta, 'w') as fichero:
            fichero.write('')
        print(f"Creado: {archivo_ruta}")

def renombra_ficheros(ruta, prefijo):
    for contenido in os.listdir(ruta):
        archivo_ruta = os.path.join(ruta, contenido)

        if os.path.isfile(archivo_ruta):
            nuevo_nombre = prefijo + contenido
            nueva_ruta = os.path.join(ruta, nuevo_nombre)

            os.rename(archivo_ruta, nueva_ruta)
            print(f"{contenido} -> {nuevo_nombre}")

def elimina_ficheros(ruta):
    for root, dirs, files in os.walk(ruta, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
            print(f"Eliminado: {os.path.join(root, file)}")
    os.rmdir(ruta)
    print(f"Archivos y directorio eliminados: {ruta}")

crea_ficheros("./ejemplo", "fichero", 10)
renombra_ficheros("./ejemplo", "prrefijo_")
elimina_ficheros("./ejemplo")