import pytest
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal
from models import Orden
from schemas import OrdenBase
import crud

def test_crear_orden():
    db: Session = SessionLocal()
    orden_data = OrdenBase(
        usuario_id=1,
        carrito_id=1,
        monto_total=100.0,
        estado="pendiente"
    )
    orden = crud.crear_orden(db, orden_data)
    assert orden.monto_total == 100.0
    db.delete(orden)
    db.commit()
    db.close()
