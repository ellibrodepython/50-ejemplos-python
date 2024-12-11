# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install matplotlib
# 2. Ejecuta el script: python 42_calcula_hipoteca.py

import matplotlib.pyplot as plt

def hipoteca(prestamo, interes, anios):
    int_mensual = interes / 1200
    num_cuotas = anios * 12
    cuota = (prestamo * int_mensual) / (1 - (1 + int_mensual) ** -num_cuotas)
    intereses = ((cuota * num_cuotas - prestamo) / prestamo) * 100
    return (cuota, intereses)

cuota, intereses = hipoteca(100000, 2, 10)
print(f"Cuota mensual: {cuota:.2f} €")
print(f"Intereses: {intereses:.2f} %")

prestado = 100000
interes = 2
plazos = range(5, 31, 5)

cuotas = [hipoteca(prestado, interes, plazo)[0] for plazo in plazos]

fig, ax1 = plt.subplots(figsize=(7, 6))
ax1.set_xlabel("Plazo (años)")
ax1.set_ylabel("Cuota mensual (€)")
ax1.plot(plazos, cuotas, label="Cuota mensual (€)")
plt.title("Cuota mensual e intereses")
plt.grid(True)
plt.show()
