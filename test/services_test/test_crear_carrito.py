import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.models import Carrito
from backend.app.logic.schemas import CarritoBase
from backend.app.crud import carritos

def test_crear_carrito():
    db: Session = SessionLocal()
    carrito_data = CarritoBase(
        usuario_id=1,
        estado="abierto"
    )
    carrito = carritos.crear_carrito(db, carrito_data)
    assert carrito.estado == "abierto"
    db.delete(carrito)
    db.commit()
    db.close()
