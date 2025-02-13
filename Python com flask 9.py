from flask import Flask, jsonify

app = Flask(__name__)
contador = 0

@app.route('/contador')
def contar():
    global contador
    contador += 1
    return jsonify({'acessos': contador})

if __name__ == '__main__':
    app.run(debug=True)
