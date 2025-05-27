import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.models import Orden
from backend.app.logic.schemas import OrdenBase
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
