# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install scikit-image matplotlib
# 2. Ejecuta el script: python 23_rotar_imagen.py
# 3. Observa el resultado de la imagen

from skimage import data
from skimage.transform import rotate
import matplotlib.pyplot as plt

imagen = data.astronaut()
imagen_rotada = rotate(imagen, angle=90, resize=True)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(imagen)
ax[1].imshow(imagen_rotada)
plt.show()