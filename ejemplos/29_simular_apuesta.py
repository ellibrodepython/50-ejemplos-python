# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install numpy
# 2. Ejecuta el script: python 29_simular_apuesta.py

import numpy as np

def apuesta(dinero_inicial, prob_ganar,
            retorno_ganar, retorno_perder, num_apuestas):
            
    dinero = [dinero_inicial]
    p = [prob_ganar, 1 - prob_ganar]
    
    for _ in range(num_apuestas):
        if np.random.choice(['Cara', 'Cruz'], p=p) == 'Cara':
            dinero.append(dinero[-1] * (1 + retorno_ganar))
        else:
            dinero.append(dinero[-1] * (1 + retorno_perder))
            
    return dinero

simulacion = apuesta(
    dinero_inicial=1000,
    prob_ganar=0.5,       # 50% probabilidad ganar
    retorno_ganar=0.8,    # +80% si ganas
    retorno_perder=-0.5,  # -50% si pierdes
    num_apuestas=20)
print(f"Dinero final (€): {simulacion[-1]:.0f}")
# Dinero final (€): 349