import pytest
from backend.product_service.service import Product, ProductService
from backend.product_service.app import app as product_app, pm as product_manager

@pytest.fixture(autouse=True)
def clear_products():
    # Limpia el estado antes y después de cada test
    product_manager.products.clear()
    yield
    product_manager.products.clear()

@pytest.fixture
def ps():
    return ProductService()

def test_unit_create_and_list(ps):
    # Test unitario de la clase ProductService
    p = Product(1, "Camisa", "Manga corta", 29.99, 50, "Ropa")
    ps.create_product(p)
    prods = ps.list_products()
    assert len(prods) == 1
    assert prods[0] is p

def test_unit_find_update_delete(ps):
    p = Product(2, "Pantalón", "Jean", 49.99, 30, "Ropa")
    ps.create_product(p)
    # find
    assert ps.find_product(2) is p
    # update
    ok = ps.update_product(2, {"price": 59.99, "stock": 20})
    assert ok
    fp = ps.find_product(2)
    assert fp.get_price() == 59.99
    assert fp.get_stock() == 20
    # delete
    ok = ps.delete_product(2)
    assert ok
    assert ps.find_product(2) is None

@pytest.fixture
def client():
    product_app.testing = True
    return product_app.test_client()

def test_integration_get_empty(client):
    resp = client.get("/products")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.get_json() == []

def test_integration_create_and_list(client):
    payload = {
        "product_id": 3,
        "name": "Gorra",
        "description": "De algodón",
        "price": 15.0,
        "stock": 100,
        "category": "Accesorios"
    }
    # crea vía HTTP
    r1 = client.post("/products", json=payload)
    assert r1.status_code == 201

    # lista vía HTTP
    r2 = client.get("/products")
    assert r2.status_code == 200
    data = r2.get_json()
    assert isinstance(data, list) and len(data) == 1
    assert data[0]["name"] == "Gorra"
