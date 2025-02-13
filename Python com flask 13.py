from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/fatorial/<int:num>')
def calcular_fatorial(num):
    return jsonify({'numero': num, 'fatorial': math.factorial(num)})

if __name__ == '__main__':
    app.run(debug=True)
