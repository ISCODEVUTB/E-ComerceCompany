import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.models import Devolucion
from backend.app.logic.schemas import DevolucionBase
from backend.app.crud import devolution

def test_crear_devolucion():
    db: Session = SessionLocal()
    devolucion_data = DevolucionBase(
        orden_id=1,
        motivo="Producto defectuoso",
        estado="pendiente"
    )
    devolucion = devolutions.crear_devolucion(db, devolucion_data)
    assert devolucion.estado == "pendiente"
    assert devolucion.motivo == "Producto defectuoso"
    db.delete(devolucion)
    db.commit()
    db.close()