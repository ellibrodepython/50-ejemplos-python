# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Ejecuta el script: python 11_patrones_re.py

import re
r1 = re.findall(r"\d+", "Tengo 2 gatos y 3 perros")
print(r1)  # ['2', '3']

r2 = re.sub(r"2", "dos", "Tengo 2 gatos y 3 perros")
r2 = re.sub(r"3", "tres", r2)
print(r2)

def valida_email(email):
    r = r"(^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$)"
    return re.match(r, email) is not None

print(valida_email("juan@gmail.com"))     # True
print(valida_email("juan@gmail.com.ar"))  # True
print(valida_email("653fsaasd"))          # False
print(valida_email("juan@gma@.dom.com"))  # False
print(valida_email("@@@"))                # False