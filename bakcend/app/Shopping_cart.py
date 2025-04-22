# -------------------------------
# 2. Shopping Cart
# -------------------------------
class ShoppingCart:
    def __init__(self, user_id):
        self._user_id = user_id
        self._items = []  # List of tuples (product, quantity)

    def add_product(self, product, quantity):
        self._items.append((product, quantity))

    def remove_product(self, product_id):
        self._items = [item for item in self._items if item[0].get_product_id() != product_id]

    def update_quantity(self, product_id, new_quantity):
        for i, (product, quantity) in enumerate(self._items):
            if product.get_product_id() == product_id:
                self._items[i] = (product, new_quantity)
                return True
        return False

    def show_summary(self):
        total = 0
        for product, quantity in self._items:
            subtotal = product.get_price() * quantity
            total += subtotal
            print(f"{product.get_name()} x{quantity} - ${subtotal}")
        print(f"Total: ${total}")