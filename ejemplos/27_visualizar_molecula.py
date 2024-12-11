# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install rdkit
# 2. Ejecuta el script: python 27_visualizar_molecula.py

from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw

smiles = 'CC(=O)OC1=CC=CC=C1C(=O)O'
molecula = Chem.MolFromSmiles(smiles)
Draw.MolToImage(molecula).show()

peso_molecular = Descriptors.MolWt(molecula)
print(f"Masa molecular aspirina: {peso_molecular:.3f} g/mol")
# Masa molecular aspirina: 180.159 g/mol