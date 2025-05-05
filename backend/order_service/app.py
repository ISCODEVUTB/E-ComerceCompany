from flask import Flask, request, jsonify
from flask_wtf import CSRFProtect
from pydantic import BaseModel
from typing import List
from werkzeug.exceptions import BadRequest
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
csrf = CSRFProtect(app)

class Order(BaseModel):
    id: int
    user_id: int
    cart_id: int
    status: str
    address: str
    total: float

orders_db: List[Order] = []

@app.route("/orders", methods=["POST"])
@csrf.exempt  # Solo mientras no se use un frontend con CSRF tokens
def create_order():
    try:
        data = request.get_json()
        order = Order(**data)
        orders_db.append(order)
        return jsonify({"message": "Order placed"}), 201
    except Exception as e:
        raise BadRequest(str(e))

@app.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):
    filtered_orders = [order.dict() for order in orders_db if order.user_id == user_id]
    return jsonify(filtered_orders), 200

@app.route("/orders/<int:order_id>", methods=["PUT"])
@csrf.exempt
def update_order(order_id):
    data = request.get_json()
    try:
        updated_order = Order(**data)
        for i, order in enumerate(orders_db):
            if order.id == order_id:
                orders_db[i] = updated_order
                return jsonify({"message": "Order updated"}), 200
        return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        raise BadRequest(str(e))

@app.route("/orders/<int:order_id>", methods=["DELETE"])
@csrf.exempt
def delete_order(order_id):
    for order in orders_db:
        if order.id == order_id:
            orders_db.remove(order)
            return jsonify({"message": "Order canceled"}), 200
    return jsonify({"error": "Order not found"}), 404
