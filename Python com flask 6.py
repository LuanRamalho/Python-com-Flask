from flask import Flask, request, jsonify
import json

app = Flask(__name__)

notes = ["Eu amo programar em python",
         "Programar em Python é tudo de bom."]

@app.route('/notes', methods=['GET'])
def get_notes():
    response = app.response_class(
        response=json.dumps(notes, ensure_ascii=False),
        status=200,
        mimetype='application/json'
    )
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/notes', methods=['POST'])
def add_note():
    new_note = request.json
    notes.append(new_note)
    response = jsonify(new_note)
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, 201

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    if 0 <= note_id < len(notes):
        response = jsonify(notes[note_id])
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    else:
        return jsonify({'error': 'Note not found'}), 404

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    if 0 <= note_id < len(notes):
        notes[note_id] = request.json
        response = jsonify(notes[note_id])
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    else:
        return jsonify({'error': 'Note not found'}), 404

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        removed_note = notes.pop(note_id)
        response = jsonify(removed_note)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    else:
        return jsonify({'error': 'Note not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
