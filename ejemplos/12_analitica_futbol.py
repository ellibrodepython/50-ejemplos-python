# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install statsbombpy seaborn matplotlib
# 2. Ejecuta el script: python 12_analitica_futbol.py

from statsbombpy import sb
import seaborn as sns
import matplotlib.pyplot as plt

ev = sb.events(match_id=3943043)
ev = ev.loc[
    (ev['type'] == "Pass") &
    (ev['team'] == "England")]

plt.figure(figsize=(9, 4))

# Representa el inicio de los pases
plt.subplot(1, 2, 1)
ax1 = sns.histplot(
    x=ev['location'].str[0],
    y=ev['location'].str[1],
    bins=(20, 20), cmap="YlGnBu", cbar=True)
ax1.set_aspect('equal', 'box')
plt.title('España/Inglaterra 14/07/2024\n'
          'Heatmap inicio de pases')

# Representa el fin de los pases
plt.subplot(1, 2, 2)
ax2 = sns.histplot(
    x=ev['pass_end_location'].str[0],
    y=ev['pass_end_location'].str[1],
    bins=(20, 20), cmap="YlGnBu", cbar=True)
ax2.set_aspect('equal', 'box')
plt.title('España/Inglaterra 14/07/2024\n'
          'Heatmap fin de pases')

plt.tight_layout()
plt.show()