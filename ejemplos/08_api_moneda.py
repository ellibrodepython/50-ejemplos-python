# Compra el libro en:
# www.ellibrodepython.com

# Instrucciones:
# 1. Instala dependencias: pip install flask
# 2. Ejecuta el script: python 08_api_moneda.py
# 3. Usa en el navegador: http://127.0.0.1:5000/to-usd/100

from flask import Flask, jsonify

app = Flask(__name__)

EUR_A_USD = 1.1

@app.route('/to-usd/<eur>', methods=['GET'])
def convert(eur):
    try:
        eur = float(eur)
        usd = eur * EUR_A_USD
        return jsonify({
            'EUR': eur,
            'USD': usd
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)