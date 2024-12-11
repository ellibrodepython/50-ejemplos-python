# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 22_benchmark_timeit.py
# 2. Observa el resultado en la consola

from timeit import timeit
from memory_profiler import memory_usage
import numpy as np


def fun_a(data, scalar):
    return [x * scalar for x in data]

def fun_b(data, scalar):
    return data * scalar

lista = list(range(10**6))
array = np.array(lista)

t_a = timeit(lambda: fun_a(lista, 5.55), number=10)
print(f"fun_a: {t_a / 10:.4f} segundos")

t_b = timeit(lambda: fun_b(array, 5.55), number=10)
print(f"fun_b: {t_b / 10:.4f} segundos")

# fun_a: 0.0360 segundos
# fun_b: 0.0010 segundos