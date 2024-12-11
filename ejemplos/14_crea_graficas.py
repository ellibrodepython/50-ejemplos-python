# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install matplotlib numpy
# 2. Ejecuta el script: python 14_crea_graficas.py

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
temperatura = np.random.normal(20, 5, 365)

fig, ax = plt.subplots(1, 2)

ax[0].plot(temperatura, label="Temperatura diaria")
ax[0].set_xlabel("Día")
ax[0].set_ylabel("Temperatura (°C)")
ax[0].set_title("Serie temporal")
ax[0].legend()

ax[1].hist(temperatura, bins=10, edgecolor="black")
ax[1].set_xlabel("Temperatura (°C)")
ax[1].set_ylabel("Frecuencia")
ax[1].set_title("Distribución")

plt.tight_layout()
plt.show()