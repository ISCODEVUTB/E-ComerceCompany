import math
import pytest
from sqlalchemy.orm import Session
from backend.app.logic.models import Producto
from backend.app.logic.schemas import ProductoBase
from backend.app.crud import product
from backend.app.logic.schemas import ProductoCreate


def test_crear_producto(db):
    # Arrange
    nuevo_producto = ProductoCreate(nombre="Laptop", descripcion="Gaming laptop", precio=1500.0, inventario=10)

    # Act
    producto_creado = product.crear_producto(db, nuevo_producto)

    # Assert
    assert producto_creado.id is not None
    assert producto_creado.nombre == "Laptop"
    assert producto_creado.descripcion == "Gaming laptop"
    assert math.isclose(producto_creado.precio, 1500.0, rel_tol=1e-9)

    # Y podemos verificar que fue insertado
    producto_en_db = product.obtener_producto_por_id(db, producto_creado.id)
    assert producto_en_db is not None
    assert producto_en_db.nombre == "Laptop"
