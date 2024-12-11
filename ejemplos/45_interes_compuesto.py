# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 45_interes_compuesto.py

def interes_compuesto(principal, interes, tiempo):
    return principal * (1 + interes) ** tiempo

principal = 1000
interes = 0.05 
tiempo = 5

interes_final = interes_compuesto(principal, interes, tiempo)
print(f"{principal} -> {interes_final:.0f} en {tiempo} años")
# 1000 -> 1276 en 5 años