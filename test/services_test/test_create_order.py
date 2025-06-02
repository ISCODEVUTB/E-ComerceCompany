import math
import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.schemas import OrdenBase, CarritoBase, UsuarioCreate
from backend.app.crud import order, cart, user

def test_crear_orden():
    db: Session = SessionLocal()
    # 1. Crear usuario
    usuario_data = UsuarioCreate(
        nombre_usuario="Test User",
        correo_electronico="test@example.com",
        rol="cliente",
        contraseña="123456"
    )
    usuario = user.crear_usuario(db, usuario_data)
    # 2. Crear carrito
    carrito_data = CarritoBase(
        usuario_id=usuario.id,
        estado="abierto"
    )
    carrito = cart.crear_carrito(db, carrito_data)
    # 3. Crear orden
    orden_data = OrdenBase(
        usuario_id=usuario.id,
        carrito_id=carrito.id,
        monto_total=100.0,
        estado="pendiente"
    )
    orden = order.crear_orden(db, orden_data)
    assert math.isclose(orden.monto_total, 100.0, rel_tol=1e-9)
    # 4. Limpiar registros
    db.delete(orden)
    db.delete(carrito)
    db.delete(usuario)
    db.commit()
    db.close()
