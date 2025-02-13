from flask import Flask, jsonify

app = Flask(__name__)

VOGAIS = 'aeiouAEIOU'

def contar_vogais(texto):
    return sum(1 for letra in texto if letra in VOGAIS)

@app.route('/vogais/<string:texto>')
def contar(texto):
    return jsonify({'texto': texto, 'total_vogais': contar_vogais(texto)})

if __name__ == '__main__':
    app.run(debug=True)
