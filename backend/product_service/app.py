from flask import Flask, jsonify, request
from service import ProductManager

app = Flask(__name__)
pm = ProductManager()

@app.route("/products", methods=["GET"])
def list_products():
    return jsonify([vars(p) for p in pm.get_all()]), 200

@app.route("/products", methods=["POST"])
def create_product():
    data = request.json
    pm.create_product(data)
    return jsonify({"msg":"Producto creado"}), 201

# rutas PUT /products/<id> y DELETE /products/<id> análogas…

if __name__ == "__main__":
    app.run(port=5001)
