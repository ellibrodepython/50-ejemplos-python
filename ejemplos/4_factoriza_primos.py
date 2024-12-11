# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 4_factoriza_primos.py

def factorizar(n):
    factores = []

    for divisor in range(2, int(n**0.5) + 1):
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor
    
    if n > 1:
        factores.append(n)
    return factores

p = 37
q = 41

factores = factorizar(p*q)
print(f"{p*q} = {'*'.join(map(str, factores))}")

numero = 10000004400000259
factores = factorizar(numero)
print(f"{numero} = {'*'.join(map(str, factores))}")