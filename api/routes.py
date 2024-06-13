from flask import Blueprint, jsonify

# Créer un Blueprint pour les routes générales de l'API
app = Blueprint('app', __name__)

# Route pour vérifier si l'API fonctionne
@app.route('/')
def index():
    return jsonify({"Welcome to the HBnB API!"})

# Vous pouvez ajouter d'autres routes générales ici si nécessaire
