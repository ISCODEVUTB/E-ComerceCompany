import os
from flask import Flask, request, jsonify
from flask_wtf import CSRFProtect
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.post("/users")
@csrf.exempt
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@app.get("/users/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.serialize())
    return jsonify({"error": "User not found"}), 404

@app.put("/users/<int:user_id>")
@csrf.exempt
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify({"message": "User updated"})

@app.delete("/users/<int:user_id>")
@csrf.exempt
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})
