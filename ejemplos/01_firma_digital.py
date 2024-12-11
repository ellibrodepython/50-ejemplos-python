# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install cryptography
# 2. Ejecuta el script: python 01_firma_digital.py

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

privada = ec.generate_private_key(ec.SECP256R1())
publica = privada.public_key()

pem = privada.private_bytes(
    serialization.Encoding.PEM,
    serialization.PrivateFormat.PKCS8,
    serialization.NoEncryption())

priv_raw = privada.private_numbers().private_value

firma = privada.sign(
    b"Envia 1 Euro al IBAN 123",
    ec.ECDSA(hashes.SHA256())
)

print(pem)
print(priv_raw)
print(firma.hex())

try:
    publica.verify(
        firma, 
        b"Envia 1 Euro al IBAN 123",
        ec.ECDSA(hashes.SHA256())
    )
    print("Verificacion OK")
except InvalidSignature:
    print("Verificacion NOK")


try:
    publica.verify( 
        firma, 
        b"Envia 100 Euro al IBAN 123",
        ec.ECDSA(hashes.SHA256())
    )
    print("Verificacion OK")
except InvalidSignature:
    print("Verificacion NOK")
