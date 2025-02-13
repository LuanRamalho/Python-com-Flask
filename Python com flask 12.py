from flask import Flask, jsonify

app = Flask(__name__)

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/primo/<int:num>')
def verificar_primo(num):
    return jsonify({'numero': num, 'E primo': eh_primo(num)})

if __name__ == '__main__':
    app.run(debug=True)
