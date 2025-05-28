from sqlalchemy.orm import Session
from backend.app.logic.models import Producto
from backend.app.logic.schemas import ProductoCreate

def obtener_productos(db: Session):
    return db.query(Producto).all()

def obtener_producto_por_id(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def crear_producto(db: Session, producto: ProductoCreate):
    nuevo_producto = Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def actualizar_producto(db: Session, producto_id: int, producto: ProductoCreate):
    producto_existente = obtener_producto_por_id(db, producto_id)
    if producto_existente:
        for key, value in producto.dict().items():
            setattr(producto_existente, key, value)
        db.commit()
        db.refresh(producto_existente)
    return producto_existente

def eliminar_producto(db: Session, producto_id: int):
    producto = obtener_producto_por_id(db, producto_id)
    if producto:
        db.delete(producto)
        db.commit()
    return producto