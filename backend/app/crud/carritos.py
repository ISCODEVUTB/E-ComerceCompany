from sqlalchemy.orm import Session
from ..models import Carrito
from ..schemas import CarritoBase

def obtener_carritos(db: Session):
    return db.query(Carrito).all()

def obtener_carrito_por_id(db: Session, carrito_id: int):
    return db.query(Carrito).filter(Carrito.id == carrito_id).first()

def crear_carrito(db: Session, carrito: CarritoBase):
    nuevo_carrito = Carrito(**carrito.dict())
    db.add(nuevo_carrito)
    db.commit()
    db.refresh(nuevo_carrito)
    return nuevo_carrito

def actualizar_carrito(db: Session, carrito_id: int, carrito: CarritoBase):
    carrito_existente = obtener_carrito_por_id(db, carrito_id)
    if carrito_existente:
        for key, value in carrito.dict().items():
            setattr(carrito_existente, key, value)
        db.commit()
        db.refresh(carrito_existente)
    return carrito_existente

def eliminar_carrito(db: Session, carrito_id: int):
    carrito = obtener_carrito_por_id(db, carrito_id)
    if carrito:
        db.delete(carrito)
        db.commit()
    return carrito