from sqlalchemy.orm import Session
from ..models import Devolucion
from ..schemas import DevolucionBase

def obtener_devoluciones(db: Session):
    return db.query(Devolucion).all()

def obtener_devolucion_por_id(db: Session, devolucion_id: int):
    return db.query(Devolucion).filter(Devolucion.id == devolucion_id).first()

def crear_devolucion(db: Session, devolucion: DevolucionBase):
    nueva_devolucion = Devolucion(**devolucion.dict())
    db.add(nueva_devolucion)
    db.commit()
    db.refresh(nueva_devolucion)
    return nueva_devolucion

def actualizar_devolucion(db: Session, devolucion_id: int, devolucion: DevolucionBase):
    devolucion_existente = obtener_devolucion_por_id(db, devolucion_id)
    if devolucion_existente:
        for key, value in devolucion.dict().items():
            setattr(devolucion_existente, key, value)
        db.commit()
        db.refresh(devolucion_existente)
    return devolucion_existente

def eliminar_devolucion(db: Session, devolucion_id: int):
    devolucion = obtener_devolucion_por_id(db, devolucion_id)
    if devolucion:
        db.delete(devolucion)
        db.commit()
    return devolucion