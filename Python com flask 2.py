from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    x = request.args.get('x')
    y = request.args.get('y')

    # Verifique se todos os parâmetros estão presentes
    if not operation or x is None or y is None:
        return jsonify({'error': 'Missing parameters'}), 400

    # Tente converter x e y para float
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

    # Realiza as operações
    if operation == 'add':
        result = x + y
    elif operation == 'subtract':
        result = x - y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'divide':
        if y == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = x / y
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
