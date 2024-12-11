# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 50_problema_mochila.py

from itertools import combinations

def obtiene_combinaciones(objetos, mochila):
    result = []
    pesos = list(objetos.values())
    nombres = list(objetos.keys())

    for r in range(1, len(pesos) + 1):
        for s_i in combinations(range(len(pesos)), r):
            s_p = [pesos[i] for i in s_i]
            if sum(s_p) == mochila:
                s_n = [nombres[i] for i in s_i]
                result.append(s_n)
    return result


objetos = {'ordenador': 5,
           'boli': 1,
           'libreta': 5,
           'peluche': 3,
           'linterna': 2,
           'chanclas': 4}

mochila = 14

combinaciones = obtiene_combinaciones(objetos, mochila)
for i in combinaciones:
    print(i)

# ['💻', '📒', '🩴']
# ['💻', '🖊', '📒', '🧸']
# ['💻', '🧸', '🔦', '🩴']
# ['📒', '🧸', '🔦', '🩴']
