from flask import Flask, request, jsonify

app = Flask(__name__)

# Taxas de câmbio fixas (exemplo simplificado)
EXCHANGE_RATES = {
    'USD': {'EUR': 0.92, 'GBP': 0.76, 'JPY': 130.45, 'BRL': 5.13},
    'EUR': {'USD': 1.09, 'GBP': 0.82, 'JPY': 141.75, 'BRL': 5.56},
    'GBP': {'USD': 1.32, 'EUR': 1.22, 'JPY': 172.75, 'BRL': 6.78},
    'JPY': {'USD': 0.0077, 'EUR': 0.007, 'GBP': 0.0058, 'BRL': 0.038},
    'BRL': {'USD': 0.20, 'EUR': 0.18, 'GBP': 0.15, 'JPY': 26.25}
}

@app.route('/')
def home():
    return "Bem-vindo à API de conversão de moedas! Use o endpoint /convert para converter valores."

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from', '').strip().upper()
    to_currency = request.args.get('to', '').strip().upper()
    amount = request.args.get('amount', '').strip()

    if not from_currency or not to_currency or not amount:
        return jsonify({'error': 'Missing parameters. Provide from, to, and amount.'}), 400

    try:
        amount = float(amount)
        if amount <= 0:
            return jsonify({'error': 'Amount must be a positive number.'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid amount. Must be a number.'}), 400

    # Verificar se as moedas estão presentes nas taxas
    if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES[from_currency]:
        return jsonify({'error': 'Invalid currency code or conversion not supported.'}), 400

    # Realizar a conversão
    rate = EXCHANGE_RATES[from_currency][to_currency]
    converted_amount = amount * rate

    return jsonify({
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
        'converted_amount': round(converted_amount, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
