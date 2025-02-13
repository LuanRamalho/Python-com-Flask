from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random')
def random_number():
    return jsonify({'numero': random.randint(1, 5000)})

if __name__ == '__main__':
    app.run(debug=True)
