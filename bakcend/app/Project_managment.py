# 1. Product and Inventory Management
# -------------------------------
class Product:
    def __init__(self, product_id, name, description, price, stock, category):
        self._product_id = product_id
        self._name = name
        self._description = description
        self._price = price
        self._stock = stock
        self._category = category

    def get_product_id(self):
        return self._product_id

    def set_product_id(self, product_id):
        self._product_id = product_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_stock(self):
        return self._stock

    def set_stock(self, stock):
        self._stock = stock

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category


class ProductService:
    def __init__(self):
        self.products = []

    def create_product(self, product):
        self.products.append(product)

    def list_products(self):
        return self.products

    def find_product(self, product_id):
        for p in self.products:
            if p.get_product_id() == product_id:
                return p
        return None

    def update_product(self, product_id, new_data):
        product = self.find_product(product_id)
        if product:
            product.set_name(new_data.get("name", product.get_name()))
            product.set_description(new_data.get("description", product.get_description()))
            product.set_price(new_data.get("price", product.get_price()))
            product.set_stock(new_data.get("stock", product.get_stock()))
            product.set_category(new_data.get("category", product.get_category()))
            return True
        return False

    def delete_product(self, product_id):
        product = self.find_product(product_id)
        if product:
            self.products.remove(product)
            return True
        return False