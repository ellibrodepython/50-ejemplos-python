# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install cryptography
# 2. Ejecuta el script: python 02_encriptar_mensaje.py

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
publica = privada.public_key()

mensaje = b"Mensaje secreto de El Libro de Python"
encriptado = publica.encrypt(
    mensaje,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None))

desencriptado = privada.decrypt(
    encriptado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None))

print(desencriptado)
# b'Mensaje secreto de El Libro de Python'