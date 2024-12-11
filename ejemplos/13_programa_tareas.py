# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install schedule
# 2. Ejecuta el script: python 13_programa_tareas.py

import schedule
import time
from datetime import datetime

def tarea():
    print(f"{datetime.now()}: Tu tarea")

schedule.every(10).minutes.do(tarea)

while True:
    schedule.run_pending()
    time.sleep(1)