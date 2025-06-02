import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.schemas import CarritoBase, UsuarioCreate
from backend.app.crud import cart, user

def test_crear_carrito():
    db: Session = SessionLocal()
    from backend.app.logic.models import Orden, Carrito, Usuario
    db.query(Orden).delete()
    db.query(Carrito).delete()
    db.query(Usuario).delete()
    db.commit()
    # 1. Crear usuario
    usuario_data = UsuarioCreate(
        nombre_usuario="Test User",
        correo_electronico="test@example.com",
        rol="cliente",
        contraseña="123456"
    )
    usuario = user.crear_usuario(db, usuario_data)
    # 2. Crear carrito con el usuario creado
    carrito_data = CarritoBase(
        usuario_id=usuario.id,
        estado="abierto"
    )
    carrito = cart.crear_carrito(db, carrito_data)
    assert carrito.estado == "abierto"
    # 3. Limpiar registros
    db.delete(carrito)
    db.delete(usuario)
    db.commit()
    db.close()
