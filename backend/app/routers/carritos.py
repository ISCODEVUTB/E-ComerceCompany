from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.crud.carritos import (
    obtener_carritos, obtener_carrito_por_id, crear_carrito,
    actualizar_carrito, eliminar_carrito
)
from backend.app.logic.schemas import Carrito, CarritoBase
from backend.app.logic.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Carrito])
def leer_carritos(db: Session = Depends(get_db)):
    return obtener_carritos(db)

@router.get("/{carrito_id}", response_model=Carrito)
def leer_carrito_por_id(carrito_id: int, db: Session = Depends(get_db)):
    carrito = obtener_carrito_por_id(db, carrito_id)
    if not carrito:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return carrito

@router.post("/", response_model=Carrito)
def crear_carrito_endpoint(carrito: CarritoBase, db: Session = Depends(get_db)):
    return crear_carrito(db, carrito)

@router.put("/{carrito_id}", response_model=Carrito)
def actualizar_carrito_endpoint(carrito_id: int, carrito: CarritoBase, db: Session = Depends(get_db)):
    carrito_actualizado = actualizar_carrito(db, carrito_id, carrito)
    if not carrito_actualizado:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return carrito_actualizado

@router.delete("/{carrito_id}", response_model=Carrito)
def eliminar_carrito_endpoint(carrito_id: int, db: Session = Depends(get_db)):
    carrito_eliminado = eliminar_carrito(db, carrito_id)
    if not carrito_eliminado:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return carrito_eliminado