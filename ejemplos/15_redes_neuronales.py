# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install tensorflow keras matplotlib numpy
# 2. Ejecuta el script: python 15_redes_neuronales.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()

plt.figure()
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f"Etiqueta: {y_train[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show(block=False)

X_train, X_test = X_train / 255.0, X_test / 255.0

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

cnn_model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

cnn_model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

cnn_model.fit(X_train, y_train,
              epochs=5, batch_size=32,
              validation_data=(X_test, y_test))

_, accuracy = cnn_model.evaluate(X_test, y_test, verbose=0)
print(f"La accuracy es: {accuracy * 100:.2f}%")
# La accuracy es: 99.23%

predicciones = cnn_model.predict(X_test[0:2])
esperado = y_test[0:2]
for p, e in zip(predicciones, esperado):
    prediccion = np.argmax(p)
    print(f"Esperado: {e}. Predicción: {prediccion}")

# Esperado: 7. Predicción: 7
# Esperado: 2. Predicción: 2