# Import nécessaire pour Flask et Flask-RestX
from flask import request
from flask_restx import Namespace, Resource, fields

# Import du DataManager
from data_manager import DataManager

# UUID et DateTime nécessaire pour l'attribut User
import uuid
from datetime import datetime

# Création d'un namespace pour la gestion des utilisateurs
ns = Namespace('users', description='Operations related to users')

# Création d'un DataManager pour le CRUD des utilisateurs
data_manager = DataManager()

# Définition du modèle pour un User
user_model = ns.model('User', {
    'id': fields.String(
        required=True,
        description='User ID'
    ),
    'username': fields.String(
        required=True,
        description='Username'
    ),
    'email': fields.String(
        required=True,
        description='Email'
    ),
    'password': fields.String(
        required=True,
        description='Password'
    ),
    'created_at': fields.DateTime(
        required=True,
        description='Date and time when the user was created'
    ),
    'updated_at': fields.DateTime(
        required=True,
        description='Date and time when the user was last updated'
    )
})

# Définition des routes pour le endpoint /users/
@ns.route('/')
class Users(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        """Fetch all users."""
        return data_manager.get_all_users()

    @ns.expect(user_model)
    @ns.response(201, 'User created successfully')
    @ns.response(400, 'Invalid request')
    def post(self):
        """Create a new user."""
        new_user_data = request.json
        
        # Vérifiez que les champs nécessaires sont présents dans la requête JSON
        if 'username' not in new_user_data or 'email' not in new_user_data or 'password' not in new_user_data:
            return {'message': 'Missing required fields'}, 400

        # Ajoutez les champs manquants (id, created_at, updated_at)
        new_user_data['id'] = str(uuid.uuid4())
        new_user_data['created_at'] = datetime.now()
        new_user_data['updated_at'] = datetime.now()

        # Essayez de sauvegarder le nouvel utilisateur avec DataManager
        try:
            user_id = data_manager.save_user(new_user_data)
            return {
                'message': 'User created successfully',
                'user_id': user_id
            }, 201
        except ValueError as e:
            return {'message': str(e)}, 400

# Définition des routes pour le endpoint /users/<user_id>
@ns.route('/<string:user_id>')
class UserResource(Resource):
    @ns.marshal_with(user_model)
    @ns.response(404, 'User not found')
    def get(self, user_id):
        """Fetch a user by their ID."""
        user_data = data_manager.get_user(user_id)
        if user_data:
            return user_data
        else:
            ns.abort(404, "User not found")

    @ns.response(204, 'User deleted successfully')
    @ns.response(404, 'User not found')
    def delete(self, user_id):
        """Delete an existing user."""
        if data_manager.delete_user(user_id):
            return '', 204
        else:
            ns.abort(404, "User not found")

    @ns.expect(user_model)
    @ns.response(204, 'User updated successfully')
    @ns.response(400, 'Invalid request')
    @ns.response(404, 'User not found')
    def put(self, user_id):
        """Update an existing user."""
        new_user_data = request.json
        new_user_data['id'] = user_id
        new_user_data['updated_at'] = datetime.now()
        if data_manager.update_user(user_id, new_user_data):
            return '', 204
        else:
            ns.abort(404, "User not found")
