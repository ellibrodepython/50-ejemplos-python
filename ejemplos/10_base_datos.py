# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install sqlite3
# 2. Ejecuta el script: python 10_bases_datos.py

import sqlite3

def conecta_db():
    return sqlite3.connect('gastos.db')

def crea_tabla():
    with conecta_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS gastos (
                categoria TEXT NOT NULL,
                cantidad REAL NOT NULL
            )''')

def add_gasto(categoria, cantidad):
    with conecta_db() as conn:
        conn.execute('''
            INSERT INTO gastos (categoria, cantidad)
            VALUES (?, ?)''', (categoria, cantidad))


def get_gastos(categoria=None):
    with conecta_db() as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM gastos WHERE '
        condiciones, parametros = [], []

        if categoria:
            condiciones.append("categoria = ?")
            parametros.append(categoria)

        query += " AND ".join(condiciones) if condiciones else "1=1"

        cursor.execute(query, parametros)
        return cursor.fetchall()
    
def total_gastos():
    with conecta_db() as conn:
        cursor = conn.cursor()
        query = 'SELECT SUM(cantidad) FROM gastos'
        cursor.execute(query)
        total = cursor.fetchone()[0]
        return total if total else 0
    
crea_tabla()
add_gasto("comida", 100)
add_gasto("transporte", 50)

gastos = get_gastos()
for gasto in gastos:
    print(gasto)

print(f"Total de gastos: {total_gastos()}")