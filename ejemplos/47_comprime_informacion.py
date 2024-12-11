# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 47_comprime_informacion.py

def comprime(s):
    comprimido = []
    cuenta = 1

    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            cuenta += 1
        else:
            comprimido.append((s[i], cuenta))
            cuenta = 1

    return comprimido

comprimido = comprime("AAAAETTTTH")
print(comprimido)
# [('A', 4), ('E', 1), ('G', 1), ('T', 3), ('H', 1)]