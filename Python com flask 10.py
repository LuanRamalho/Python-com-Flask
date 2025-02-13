from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/converter/<float:valor>/<string:unidade>')
def converter_temperatura(valor, unidade):
    if unidade == 'celsius':
        resultado = (valor * 9/5) + 32
        unidade_destino = 'fahrenheit'
    elif unidade == 'fahrenheit':
        resultado = (valor - 32) * 5/9
        unidade_destino = 'celsius'
    else:
        return jsonify({'erro': 'Unidade inválida. Use "celsius" ou "fahrenheit".'})
    
    return jsonify({'valor_original': valor, 'convertido': resultado, 'unidade': unidade_destino})

if __name__ == '__main__':
    app.run(debug=True)
