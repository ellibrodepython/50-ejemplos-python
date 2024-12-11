# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 34_barajar_cartas.py

import itertools
import random

palos = ['Picas', 'Corazones', 'Tréboles', 'Diamantes']
numeros = ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']
baraja = list(itertools.product(numeros, palos))

def baraja_cartas(baraja):
    n = len(baraja)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        baraja[i], baraja[j] = baraja[j], baraja[i]

# Baraja con nuestra funcion
baraja_cartas(baraja)

for carta in baraja:
    print(f"{carta[0]} de {carta[1]}")

# Baraja con la funcion shuffle
random.shuffle(baraja)

for carta in baraja:
    print(f"{carta[0]} de {carta[1]}")
