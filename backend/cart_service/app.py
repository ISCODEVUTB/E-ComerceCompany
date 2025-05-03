from flask import Flask, request, jsonify
from flask_wtf import CSRFProtect
from backend.cart_service.service import ShoppingCart
from backend.product_service.service import Product

app = Flask(__name__)
app.config['7777'] = '7777'
csrf = CSRFProtect(app)

carts = {}

def get_cart(user_id):
    if user_id not in carts:
        carts[user_id] = ShoppingCart(user_id)
    return carts[user_id]

@app.route("/cart/<user_id>/items", methods=["GET"])
def list_cart_items(user_id):
    cart = get_cart(user_id)
    items = []
    for product, quantity in cart._items:
        items.append({
            "product_id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "quantity": quantity
        })
    total = sum(product.get_price() * qty for product, qty in cart._items)
    return jsonify({"items": items, "total": total}), 200

@app.route("/cart/<user_id>/items", methods=["POST"])
def add_item(user_id):
    data = request.json

    product = Product(
        data["product_id"],
        data.get("name", ""),
        data.get("description", ""),
        data.get("price", 0),
        data.get("stock", 0),
        data.get("category", "")
    )
    quantity = data.get("quantity", 1)
    cart = get_cart(user_id)
    cart.add_product(product, quantity)
    return jsonify({"message": "Product added to cart"}), 201

@app.route("/cart/<user_id>/items/<int:product_id>", methods=["PUT"])
def update_item(user_id, product_id):
    data = request.json
    new_qty = data.get("quantity")
    cart = get_cart(user_id)
    if cart.update_quantity(product_id, new_qty):
        return jsonify({"message": "Quantity updated"}), 200
    return jsonify({"error": "Product not found in cart"}), 404

@app.route("/cart/<user_id>/items/<int:product_id>", methods=["DELETE"])
def delete_item(user_id, product_id):
    cart = get_cart(user_id)
    cart.remove_product(product_id)
    return jsonify({"message": "Product removed from cart"}), 200

if __name__ == "__main__":
    app.run(port=5002, debug=True)
