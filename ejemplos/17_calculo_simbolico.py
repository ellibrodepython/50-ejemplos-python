# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install sympy
# 2. Ejecuta el script: python 17_calculo_simbolico.py

import sympy as sp

x = sp.symbols('x')
p = x**3 + 3*x + 10

print(p)
# x**3 + 3*x + 10

print("Derivada:", sp.diff(p, x))
# Derivada: 3*x**2 + 3

print("Integral:", sp.integrate(p, x))
# Integral: x**4/4 + 3*x**2/2 + 10*x