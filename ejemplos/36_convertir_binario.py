# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 36_convertir_binario.py

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        if digito not in {'0', '1'}:
            raise ValueError("El número binario no es válido.")
        decimal += int(digito) * (2 ** potencia)
        potencia += 1

    return decimal


binario = "11011"
decimal = binario_a_decimal(binario)
print(f"{binario} -> {decimal}")
# 11011 -> 27