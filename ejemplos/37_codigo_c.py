# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install cffi
# 2. Asegurate de tener el archivo codigo_c.c en el mismo directorio
# 3. Ejecuta el script: python 37_codigo_c.py

import cffi
import os

if not os.path.exists("mylib.o"):
    ffi = cffi.FFI()
    ffi.cdef("bool es_primo(int n);")
    ffi.set_source(
        "_mylib",
        '#include "37_codigo_c.c"')
    ffi.compile()

import _mylib
numero = 777
primo = _mylib.lib.es_primo(numero)
print(f"El {numero}{'' if primo else ' no'} es primo")