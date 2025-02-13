from flask import Flask, jsonify

app = Flask(__name__)

def fibonacci(n):
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

@app.route('/fibonacci/<int:n>')
def gerar_fibonacci(n):
    return jsonify({'quantidade': n, 'sequencia': fibonacci(n)})

if __name__ == '__main__':
    app.run(debug=True)
