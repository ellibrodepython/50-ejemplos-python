# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala las librerías necesarias: pip install wordcloud matplotlib
# 2. Ejecuta el script: python 43_quijote_wordcloud.py

from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("43_quijote_wordcloud.txt", "r", encoding="utf-8") as file:
    quijote = file.read()

wc = WordCloud(background_color="white", width=700, height=400)
wc.generate(quijote)

plt.figure(figsize=(10, 5))
plt.imshow(wc)
plt.axis("off")
plt.tight_layout()
plt.show()