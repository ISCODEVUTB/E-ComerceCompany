import pytest
from backend.cart_service.service import ShoppingCart, Product
from backend.cart_service.app import app as cart_app, carts as carts_store

@pytest.fixture(autouse=True)
def clear_carts():
    # Asegura que el store en memoria esté limpio
    carts_store.clear()
    yield
    carts_store.clear()

@pytest.fixture
def cs():
    return ShoppingCart(user_id=99)

def test_unit_add_remove_update(cs):
    # unit tests de ShoppingCart
    prod = Product(1, "Libro", "Historia", 12.5, 20, "Libros")
    cs.add_product(prod, 2)
    assert len(cs._items) == 1
    # update
    ok = cs.update_quantity(1, 5)
    assert ok and cs._items[0][1] == 5
    # remove
    cs.remove_product(1)
    assert cs._items == []

def test_unit_show_summary(capsys, cs):
    prod = Product(2, "Taza", "Cerámica", 5.0, 10, "Hogar")
    cs.add_product(prod, 3)
    cs.show_summary()
    captured = capsys.readouterr().out
    assert "Taza x3 - $15.0" in captured
    assert "Total: $15.0" in captured

@pytest.fixture
def client():
    cart_app.testing = True
    return cart_app.test_client()

def test_integration_empty_cart(client):
    resp = client.get("/cart/42/items")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["items"] == []
    assert data["total"] == 0

def test_integration_add_and_list_item(client):
    item = {
        "product_id": 5,
        "name": "Lápiz",
        "description": "Grafito",
        "price": 1.5,
        "stock": 100,
        "category": "Papelería",
        "quantity": 4
    }
    r1 = client.post("/cart/42/items", json=item)
    assert r1.status_code == 201

    r2 = client.get("/cart/42/items")
    data = r2.get_json()
    assert len(data["items"]) == 1
    assert data["items"][0]["product_id"] == 5
    assert data["total"] == 6.0

def test_integration_update_and_delete_item(client):
    # primero añade
    client.post("/cart/7/items", json={
        "product_id": 6, "name":"Vaso","description":"Vidrio","price":3.0,"stock":50,"category":"Cocina","quantity":2
    })
    # actualiza cantidad
    r2 = client.put("/cart/7/items/6", json={"quantity": 5})
    assert r2.status_code == 200
    d2 = client.get("/cart/7/items").get_json()
    assert d2["items"][0]["quantity"] == 5
    assert d2["total"] == 15.0
    # elimina
    r3 = client.delete("/cart/7/items/6")
    assert r3.status_code == 200
    d3 = client.get("/cart/7/items").get_json()
    assert d3["items"] == []
    assert d3["total"] == 0
