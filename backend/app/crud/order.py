from sqlalchemy.orm import Session
from backend.app.logic.models import Orden
from backend.app.logic.schemas import OrdenBase

def obtener_ordenes(db: Session):
    return db.query(Orden).all()

def obtener_orden_por_id(db: Session, orden_id: int):
    return db.query(Orden).filter(Orden.id == orden_id).first()

def crear_orden(db: Session, orden: OrdenBase):
    nueva_orden = Orden(**orden.model_dump())
    db.add(nueva_orden)
    db.commit()
    db.refresh(nueva_orden)
    return nueva_orden

def actualizar_orden(db: Session, orden_id: int, orden: OrdenBase):
    orden_existente = obtener_orden_por_id(db, orden_id)
    if orden_existente:
        for key, value in orden.model_dump().items():
            setattr(orden_existente, key, value)
        db.commit()
        db.refresh(orden_existente)
    return orden_existente

def eliminar_orden(db: Session, orden_id: int):
    orden = obtener_orden_por_id(db, orden_id)
    if orden:
        db.delete(orden)
        db.commit()
    return orden