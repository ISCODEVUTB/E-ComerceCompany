from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.crud.productos import (
    obtener_productos, obtener_producto_por_id, crear_producto,
    actualizar_producto, eliminar_producto
)
from backend.app.logic.schemas import Producto, ProductoCreate
from backend.app.logic.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Producto])
def leer_productos(db: Session = Depends(get_db)):
    return obtener_productos(db)

@router.get("/{producto_id}", response_model=Producto)
def leer_producto_por_id(producto_id: int, db: Session = Depends(get_db)):
    producto = obtener_producto_por_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=Producto)
def crear_producto_endpoint(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crear_producto(db, producto)

@router.put("/{producto_id}", response_model=Producto)
def actualizar_producto_endpoint(producto_id: int, producto: ProductoCreate, db: Session = Depends(get_db)):
    producto_actualizado = actualizar_producto(db, producto_id, producto)
    if not producto_actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_actualizado

@router.delete("/{producto_id}", response_model=Producto)
def eliminar_producto_endpoint(producto_id: int, db: Session = Depends(get_db)):
    producto_eliminado = eliminar_producto(db, producto_id)
    if not producto_eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_eliminado