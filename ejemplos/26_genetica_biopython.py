# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install biopython
# 2. Ejecuta el script: python 26_genetica_biopython.py

from Bio.Seq import Seq

adn = Seq("ATGGCCATTGTAATGGGC")
print(f"ADN: {adn}")
# ADN: ATGGCCATTGTAATGGGC

adn_compl = adn.complement()
print(f"Complementaria: {adn_compl}")
# Complementaria: TACCGGTAACATTACCCG

arn = adn.transcribe()
print(f"Secuencia ARN: {arn}")
# ARN: AUGGCCAUUGUAAUGGGC

proteina = arn.translate()
print(f"Proteina: {proteina}")
# Proteina: MAIVMG