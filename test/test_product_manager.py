import pytest
from bakcend.product_service.service import ProductManager, Product

@pytest.fixture
def pm():
    return ProductManager()

def test_create_and_find(pm):
    data = {"product_id":1, "name":"Zapato", "description":"...", "price":50, "stock":10, "category":"Calzado"}
    pm.create_product(data)
    p = pm.find_product(1)
    assert isinstance(p, Product)
    assert p.get_name() == "Zapato"

def test_update_and_delete(pm):
    pm.create_product({"product_id":2, "name":"Bota", "description":"...", "price":80, "stock":5, "category":"Calzado"})
    assert pm.update_product(2, {"price":90}) is True
    assert pm.find_product(2).get_price() == 90
    assert pm.delete_product(2) is True
    assert pm.find_product(2) is None
