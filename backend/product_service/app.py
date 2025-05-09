import os
from flask import Flask, jsonify, request
from flask_wtf import CSRFProtect
from backend.product_service.service import ProductService
pm = ProductService()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']
csrf = CSRFProtect(app)

pm = ProductService()

@app.route("/products", methods=["GET"])
def list_products():
    return jsonify(pm.list_products()), 200

@app.route("/products", methods=["POST"])
def create_product():
    data = request.json
    pm.create_product(data)
    return jsonify({"msg":"Producto creado"}), 201


if __name__ == "__main__":
    app.run(port=5001)
