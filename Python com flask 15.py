from flask import Flask, jsonify

app = Flask(__name__)

def eh_palindromo(texto):
    texto_limpo = ''.join(c for c in texto.lower() if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

@app.route('/palindromo/<string:texto>')
def verificar_palindromo(texto):
    return jsonify({'texto': texto, 'E palindromo': eh_palindromo(texto)})

if __name__ == '__main__':
    app.run(debug=True)
