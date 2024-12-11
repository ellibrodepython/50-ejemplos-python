# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install numpy
# 2. Ejecuta el script: python 28_polinomios_numpy.py

from itertools import zip_longest
import numpy as np

def suma(p, q):
    return [pp+qq for pp, qq in zip_longest(p, q, fillvalue=0)]

def resta(p, q):
    return [pp-qq for pp, qq in zip_longest(p, q, fillvalue=0)]

def multiplica(p, q):
    grado = len(p) + len(q) - 2
    resultado = [0] * (grado + 1)

    for i, pp in enumerate(p):
        for j, qq in enumerate(q):
            resultado[i + j] += pp * qq

    return resultado


def evalua(p, x):
    resultado = 0
    for coef in reversed(p):
        resultado = resultado * x + coef
    return resultado


p = [1, 0, 3]
q = [5, 1, 2]

print("Con nuestras funciones")
print(suma(p, q))
print(resta(p, q))
print(multiplica(p, q))
print(evalua(p, 5))

print("Con numpy")
print(np.polynomial.polynomial.polyadd(p, q))
print(np.polynomial.polynomial.polysub(p, q))
print(np.polynomial.polynomial.polymul(p, q))
print(np.polynomial.polynomial.polyval(5, p))
