import os
from flask import Flask, request, jsonify
from flask_wtf import CSRFProtect
from backend.user_service.service import UserService, User

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-key')
csrf = CSRFProtect(app)

srv = UserService()

@app.route('/users', methods=['POST'])
@csrf.exempt
def create_user():
    data = request.json
    user = User(**data)
    srv.create(user)
    return jsonify({'message': 'User created'}), 201

@app.route('/users', methods=['GET'])
def list_users():
    users = srv.list()
    return jsonify([u.dict() for u in users]), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = srv.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.dict()), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
@csrf.exempt
def update_user(user_id):
    data = request.json
    new_user = User(**data)
    ok = srv.update(user_id, new_user)
    if not ok:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User updated'}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
@csrf.exempt
def delete_user(user_id):
    ok = srv.delete(user_id)
    if not ok:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port, debug=True)
