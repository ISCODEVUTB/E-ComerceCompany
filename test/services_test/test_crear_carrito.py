import pytest
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal
from models import Carrito
from schemas import CarritoBase
import crud

def test_crear_carrito():
    db: Session = SessionLocal()
    carrito_data = CarritoBase(
        usuario_id=1,
        estado="abierto"
    )
    carrito = crud.crear_carrito(db, carrito_data)
    assert carrito.estado == "abierto"
    db.delete(carrito)
    db.commit()
    db.close()
