import pytest
from backend.order_service.app import app, orders_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    orders_db.clear()

@pytest.fixture
def sample_order():
    return {
        "id": 1,
        "user_id": 1,
        "cart_id": 10,
        "status": "pending",
        "address": "123 Main St",
        "total": 100.0
    }

def test_create_and_get_order(client, sample_order):
    response = client.post("/orders", json=sample_order)
    assert response.status_code == 201

    response = client.get("/orders/1")
    assert response.status_code == 200
    orders = response.get_json()
    assert len(orders) == 1
    assert orders[0]["address"] == "123 Main St"

def test_update_and_delete_order(client, sample_order):
    client.post("/orders", json=sample_order)

    updated_order = sample_order.copy()
    updated_order["status"] = "shipped"
    response = client.put("/orders/1", json=updated_order)
    assert response.status_code == 200

    response = client.delete("/orders/1")
    assert response.status_code == 200
