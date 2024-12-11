# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install flask
# 2. Ejecuta el script: python 07_acortar_enlaces.py
# 3. En otra terminal, ejecuta: curl -X POST -d "url=https://www.google.com" http://127.0.0.1:5000/acorta
# 4. Comprueba el resultado: http://127.0.0.1:5000/acortada

from flask import Flask, request, redirect
import hashlib

app = Flask(__name__)
url_map = {}

@app.route('/acorta', methods=['POST'])
def shorten_url():
    url_larga = request.form['url']
    url_corta = acorta_url(url_larga)
    url_map[url_corta] = url_larga
    return f'Acortada: {url_larga} -> {url_corta}'

@app.route('/<url_corta>')
def corta_a_larga(url_corta):
    url_larga = url_map.get(url_corta)
    if url_larga:
        return redirect(url_larga)
    else:
        return 'No encontrada!', 404

def acorta_url(full_url):
    hashed = hashlib.sha256(full_url.encode()).hexdigest()
    return hashed[:7]

if __name__ == '__main__':
    app.run(debug=True)