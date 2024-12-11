# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 40_calcular_impuestos.py

TRAMOS = [
    (12000, 0.19),
    (20000, 0.24),
    (30000, 0.30),
    (60000, 0.37),
    (float('inf'), 0.45)]

def impuesto(ingreso):
    impuesto = 0

    for i, (hasta, tax) in enumerate(TRAMOS):
        desde = TRAMOS[i - 1][0] if i > 0 else 0
        tramo = min(ingreso, hasta) - desde
        if tramo > 0:
            impuesto += tramo * tax
        if ingreso <= hasta:
            break

    return impuesto


total_impuesto = impuesto(ingreso = 100000)
print(f"El impuesto es {total_impuesto:.2f}")