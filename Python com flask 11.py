from flask import Flask, jsonify
import uuid

app = Flask(__name__)

@app.route('/uuid')
def gerar_uuid():
    return jsonify({'uuid': str(uuid.uuid4())})

if __name__ == '__main__':
    app.run(debug=True)
