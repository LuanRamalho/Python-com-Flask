from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = ["Fulano", "Deltrano", "Ciclano"]

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    new_contact = request.json
    contacts.append(new_contact)
    return jsonify(new_contact), 201

@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    if 0 <= contact_id < len(contacts):
        return jsonify(contacts[contact_id])
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    if 0 <= contact_id < len(contacts):
        contacts[contact_id] = request.json
        return jsonify(contacts[contact_id])
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    if 0 <= contact_id < len(contacts):
        removed_contact = contacts.pop(contact_id)
        return jsonify(removed_contact)
    else:
        return jsonify({'error': 'Contact not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

