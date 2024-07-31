from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from services.auth_service import UserService
from forms.registration_form import RegistrationForm
from utils.decorator import handle_errors

auth_bp = Blueprint('auths', __name__)

@auth_bp.route('/register', methods=['POST'])
@handle_errors
def register():
    form = RegistrationForm(data=request.json)
    if not form.validate():
        raise BadRequest(description=form.errors)

    user = UserService.create_user(form)
    return jsonify({'message': 'User created successfully', 'user': user.username}), 201

@auth_bp.route('/login', methods=['POST'])
@handle_errors
def login():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        raise BadRequest("Username and password are required.")
    
    user = UserService.verify_user(data['username'], data['password'])
    return jsonify({'message': 'Login successful', 'user': user.username}), 200
