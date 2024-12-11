# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 03_numero_primo.py

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = 37
b = 41
c = 10

print(f"{a} es primo? {es_primo(a)}")
print(f"{b} es primo? {es_primo(b)}")
print(f"{c} es primo? {es_primo(c)}")

