from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.crud.devolutions import (
    obtener_devoluciones, obtener_devolucion_por_id, crear_devolucion,
    actualizar_devolucion, eliminar_devolucion
)
from backend.app.logic.schemas import Devolucion, DevolucionBase
from backend.app.logic.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Devolucion])
def leer_devoluciones(db: Session = Depends(get_db)):
    return obtener_devoluciones(db)

@router.get("/{devolucion_id}", response_model=Devolucion)
def leer_devolucion_por_id(devolucion_id: int, db: Session = Depends(get_db)):
    devolucion = obtener_devolucion_por_id(db, devolucion_id)
    if not devolucion:
        raise HTTPException(status_code=404, detail="Devolución no encontrada")
    return devolucion

@router.post("/", response_model=Devolucion)
def crear_devolucion_endpoint(devolucion: DevolucionBase, db: Session = Depends(get_db)):
    return crear_devolucion(db, devolucion)

@router.put("/{devolucion_id}", response_model=Devolucion)
def actualizar_devolucion_endpoint(devolucion_id: int, devolucion: DevolucionBase, db: Session = Depends(get_db)):
    devolucion_actualizada = actualizar_devolucion(db, devolucion_id, devolucion)
    if not devolucion_actualizada:
        raise HTTPException(status_code=404, detail="Devolución no encontrada")
    return devolucion_actualizada

@router.delete("/{devolucion_id}", response_model=Devolucion)
def eliminar_devolucion_endpoint(devolucion_id: int, db: Session = Depends(get_db)):
    devolucion_eliminada = eliminar_devolucion(db, devolucion_id)
    if not devolucion_eliminada:
        raise HTTPException(status_code=404, detail="Devolución no encontrada")
    return devolucion_eliminada