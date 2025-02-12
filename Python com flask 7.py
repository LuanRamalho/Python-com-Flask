from flask import Flask, request, jsonify

app = Flask(__name__)

conversion_factors = {
    'length': {
        'meters_to_kilometers': 0.001,
        'kilometers_to_meters': 1000,
        'meters_to_miles': 0.000621371,
        'miles_to_meters': 1609.34,
        'kilometers_to_miles': 0.621371,
        'miles_to_kilometers': 1.60934,
    },
    'weight': {
        'grams_to_kilograms': 0.001,
        'kilograms_to_grams': 1000,
        'grams_to_pounds': 0.00220462,
        'pounds_to_grams': 453.592,
        'pounds_to_kilograms': 0.453592,  
        'kilograms_to_pounds': 2.20462,   
    }
}


@app.route('/convert', methods=['GET'])
def convert_units():
    category = request.args.get('category')
    from_unit = request.args.get('from')
    to_unit = request.args.get('to')
    value = request.args.get('value')

    if not category or not from_unit or not to_unit or value is None:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        value = float(value)  # agora convertendo para float após verificar se não é None
        factor = conversion_factors[category][f'{from_unit}_to_{to_unit}']
        converted_value = value * factor
        return jsonify({'converted_value': converted_value})
    except KeyError:
        return jsonify({'error': 'Invalid conversion parameters'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid value provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
