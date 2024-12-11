# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script con "python 39cuenta_atras.py"

import time
import sys

def cuenta_atras(segundos):
    for queda in range(segundos, 0, -1):
        progreso = int((segundos - queda) / segundos * 30)
        barra = f"[{'=' * progreso}{' ' * (30 - progreso)}]"
        sys.stdout.write(f"\r{barra} {queda}s restantes...")
        sys.stdout.flush()
        time.sleep(1)
    print("\r[==============================] Completado!      ")

cuenta_atras(10)