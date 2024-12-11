# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 33_baraja_poker.py

import itertools

palos = ['Picas', 'Corazones', 'Tréboles', 'Diamantes']
numeros = ['A'] + list(range(2, 11)) + ['J', 'Q', 'K']

baraja = list(itertools.product(numeros, palos))

for carta in baraja:
    print(f"{carta[0]} de {carta[1]}")

# A de Picas
# A de Corazones
# A de Tréboles
# A de Diamantes
# ...
