
import pytest
from backend.cart_service.app import app, carts

@pytest.fixture(autouse=True)
def clear_carts():
    # Antes de cada test
    carts.clear()
    yield
    carts.clear()

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_list_empty_cart(client):
    resp = client.get("/cart/42/items")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["items"] == []
    assert data["total"] == 0

def test_add_and_list_item(client):
    item = {
        "product_id": 1,
        "name": "Libro",
        "description": "Historia",
        "price": 15.0,
        "stock": 50,
        "category": "Libros",
        "quantity": 2
    }
    resp = client.post("/cart/42/items", json=item)
    assert resp.status_code == 201

    resp = client.get("/cart/42/items")
    data = resp.get_json()
    assert len(data["items"]) == 1
    assert data["items"][0]["product_id"] == 1
    assert data["total"] == 30.0

def test_update_and_delete_item(client):
    # Añade primero
    client.post("/cart/7/items", json={
        "product_id": 3, "name":"Taza","description":"Cerámica","price":5.0,"stock":20,"category":"Hogar","quantity":1
    })

    # PUT actualiza cantidad a 4
    resp = client.put("/cart/7/items/3", json={"quantity": 4})
    assert resp.status_code == 200
    data = client.get("/cart/7/items").get_json()
    assert data["items"][0]["quantity"] == 4
    assert data["total"] == 20.0

    # DELETE elimina
    resp = client.delete("/cart/7/items/3")
    assert resp.status_code == 200
    data = client.get("/cart/7/items").get_json()
    assert data["items"] == []
    assert data["total"] == 0
