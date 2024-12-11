# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install numpy matplotlib
# 2. Ejecuta el script: python 30_montecarlo_numpy.py

import numpy as np
import matplotlib.pyplot as plt

def simula_portfolio(
        inicial, retorno_anual,
        volatilidad_anual, tiempo_anios,
        simulaciones):

    np.random.seed(42)
    retornos = np.random.normal(retorno_anual, volatilidad_anual, (tiempo_anios, simulaciones))
    valor_portfolio = inicial * (1 + retornos).cumprod(axis=0)

    plt.figure()
    plt.plot(valor_portfolio, alpha=0.5)
    plt.title("Simulación Monte Carlo de Portfolio")
    plt.xlabel("Año")
    plt.ylabel("Valor Portfolio (€)")
    plt.grid(True)

    mejor_caso = valor_portfolio.max(axis=1)[-1]
    peor_caso = valor_portfolio.min(axis=1)[-1]
    plt.text(tiempo_anios / 2, mejor_caso / 2,
             f'Mejor caso: {mejor_caso:.0f}€'+f'\nPeor caso: {peor_caso:.0f}€', 
             bbox=dict(facecolor='grey', alpha=0.9))

    plt.show()

simula_portfolio(
    inicial=100_000,
    retorno_anual=0.07,
    volatilidad_anual=0.04,
    tiempo_anios=20,
    simulaciones=100)