import os, sys
import pytest

# Ajusta PYTHONPATH para localizar los módulos del microservicio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app')))

from Shopping_cart import ShoppingCart
from Project_managment import Product

@pytest.fixture
def cart():
    return ShoppingCart(user_id=123)

@pytest.fixture
def sample_product():
    # Crea un producto de ejemplo para añadir al carrito
    return Product(1, "Libro", "Un libro interesante", 20.0, 100, "Libros")

def test_add_product(cart, sample_product):
    cart.add_product(sample_product, 2)
    assert len(cart._items) == 1
    prod, qty = cart._items[0]
    assert prod is sample_product
    assert qty == 2

def test_remove_product(cart, sample_product):
    cart.add_product(sample_product, 3)
    cart.remove_product(sample_product.get_product_id())
    assert len(cart._items) == 0

def test_update_quantity(cart, sample_product):
    cart.add_product(sample_product, 5)
    # Actualiza la cantidad a 2
    assert cart.update_quantity(sample_product.get_product_id(), 2)
    prod, qty = cart._items[0]
    assert qty == 2

def test_update_nonexistent(cart):
    # Intentar actualizar un producto que no existe debe devolver False
    assert not cart.update_quantity(999, 1)

def test_show_summary(capsys, cart, sample_product):
    # Verifica la salida por terminal de show_summary()
    cart.add_product(sample_product, 3)
    cart.show_summary()
    captured = capsys.readouterr()
    assert "Libro x3 - $60.0" in captured.out
    assert "Total: $60.0" in captured.out
