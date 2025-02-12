from flask import Flask, request, jsonify
import string
import random

app = Flask(__name__)

# Rota principal para evitar erro 404 ao acessar /
@app.route('/')
def home():
    return "Bem-vindo à API de geração de senhas! Use o endpoint /generate_password para gerar uma senha."

@app.route('/generate_password', methods=['GET'])
def generate_password():
    # Verifica se 'length' é um número válido
    try:
        length = int(request.args.get('length', 12))
    except ValueError:
        return jsonify({'error': 'Invalid length parameter'}), 400

    include_uppercase = request.args.get('include_uppercase', 'true').lower() == 'true'
    include_numbers = request.args.get('include_numbers', 'true').lower() == 'true'
    include_special = request.args.get('include_special', 'true').lower() == 'true'

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Garante que há pelo menos um tipo de caractere para evitar erros
    if not characters:
        return jsonify({'error': 'No characters selected for password'}), 400

    password = ''.join(random.choice(characters) for _ in range(length))

    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
