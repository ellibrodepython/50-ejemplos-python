# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 38_martingala.py

import random

def martingala(inicial, apuesta, prob_ganar, objetivo):
    balance = inicial
    bet = apuesta

    while balance > 0 and balance < inicial + objetivo:
        rojo = random.random() < prob_ganar
        if rojo:
            balance -= bet
            bet *= 2
        else:
            balance += bet
            bet = apuesta

        if bet > balance:
            break

    return balance

print(martingala(inicial=1000,
                 apuesta=10,
                 prob_ganar=0.48,
                 objetivo=2000))