# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 6_fuerza_bruta.py

import itertools

def fuerza_bruta(contrasenia, long_max=6):
    c = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    for longitud in range(1, long_max + 1):
        print(f"Intentando con longitud {longitud}...")
        for intento in itertools.product(c, repeat=longitud):
            intento_s = ''.join(intento)
            if intento_s == contrasenia:
                return intento_s
    return None


contrasenia = "pass67"
encontrada = fuerza_bruta(contrasenia, long_max=8)
print(f"Contraseña encontrada: {encontrada}")