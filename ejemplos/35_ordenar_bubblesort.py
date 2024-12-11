# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 35_ordenar_bubblesort.py

def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                # Pista: Puede optimizarse
    return l

l = [64, 34, 25, 12, 22, 11, 90]
l_ordenado = bubble_sort(l)
print("Ordenado:", l_ordenado)
