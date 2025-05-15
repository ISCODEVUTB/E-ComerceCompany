from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud.ordenes import (
    obtener_ordenes, obtener_orden_por_id, crear_orden,
    actualizar_orden, eliminar_orden
)
from ..schemas import Orden, OrdenBase
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[Orden])
def leer_ordenes(db: Session = Depends(get_db)):
    return obtener_ordenes(db)

@router.get("/{orden_id}", response_model=Orden)
def leer_orden_por_id(orden_id: int, db: Session = Depends(get_db)):
    orden = obtener_orden_por_id(db, orden_id)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden

@router.post("/", response_model=Orden)
def crear_orden_endpoint(orden: OrdenBase, db: Session = Depends(get_db)):
    return crear_orden(db, orden)

@router.put("/{orden_id}", response_model=Orden)
def actualizar_orden_endpoint(orden_id: int, orden: OrdenBase, db: Session = Depends(get_db)):
    orden_actualizada = actualizar_orden(db, orden_id, orden)
    if not orden_actualizada:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden_actualizada

@router.delete("/{orden_id}", response_model=Orden)
def eliminar_orden_endpoint(orden_id: int, db: Session = Depends(get_db)):
    orden_eliminada = eliminar_orden(db, orden_id)
    if not orden_eliminada:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden_eliminada