from flask import Flask, request, jsonify
from model.user import User
from persistence.user_dao import UserDAO

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(data['user_id'], data['email'], data['name'])
    UserDAO.save(user)
    return jsonify({'message': 'Utilisateur créé'}), 201

# Ajoutez d'autres endpoints pour les opérations CRUD...

if __name__ == '__main__':
    app.run(debug=True)
