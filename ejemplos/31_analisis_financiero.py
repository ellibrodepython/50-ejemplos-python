# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install yfinance numpy matplotlib pandas
# 2. Ejecuta el script: python 31_analisis_financiero.py

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

apple = yf.download('AAPL', start='2020-01-01', end='2021-01-01')

apple['9_MA'] = apple['Close'].rolling(window=9).mean()
apple['20_MA'] = apple['Close'].rolling(window=20).mean()

apple['Signal'] = np.where(apple['9_MA'] > apple['20_MA'], 1.0, 0.0)
apple['Position'] = apple['Signal'].diff()

plt.figure()
plt.plot(apple['Close'], label='Precio Apple', alpha=0.5)
plt.plot(apple['9_MA'], label='Media 9 días', alpha=0.8)
plt.plot(apple['20_MA'], label='Media 20 días', alpha=0.8)

plt.plot(apple.index,
         np.where(apple['Position'] == 1, apple['9_MA'], np.nan),
         '^', markersize=10, color='g', lw=0, label='Compra')

plt.plot(apple.index,
         np.where(apple['Position'] == -1, apple['9_MA'], np.nan),
         'v', markersize=10, color='r', lw=0, label='Vende')

plt.title('Valor acción Apple')
plt.legend(loc='best')
plt.show()