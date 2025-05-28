import pytest
from backend.app.logic.models import Producto
from backend.app.logic.schemas import ProductoBase
from backend.app.crud import productos
from backend.app.logic.schemas import ProductoCreate


def test_crear_producto(db):
    # Arrange
    nuevo_producto = productos.ProductoCreate(nombre="Laptop", descripcion="Gaming laptop", precio=1500.0)

    # Act
    producto_creado = productos.crear_producto(db, nuevo_producto)

    # Assert
    assert producto_creado.id is not None
    assert producto_creado.nombre == "Laptop"
    assert producto_creado.descripcion == "Gaming laptop"
    assert producto_creado.precio == 1500.0

    # Y podemos verificar que fue insertado
    producto_en_db = productos.obtener_producto_por_id(db, producto_creado.id)
    assert producto_en_db is not None
    assert producto_en_db.nombre == "Laptop"
