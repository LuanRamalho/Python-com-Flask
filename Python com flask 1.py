from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à página inicial desse programa python com flask."

@app.route('/saudacao', methods=['GET'])
def saudacao():
    nome = request.args.get('nome', 'Mundo')
    return f"Olá, {nome}!"

if __name__ == '__main__':
    app.run(debug=True)