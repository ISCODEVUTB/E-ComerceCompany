from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.crud.user import (
    obtener_usuarios, obtener_usuario_por_id, crear_usuario,
    actualizar_usuario, eliminar_usuario
)
from backend.app.logic.schemas import Usuario, UsuarioCreate
from backend.app.logic.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Usuario])
def leer_usuarios(db: Session = Depends(get_db)):
    return obtener_usuarios(db)


@router.get("/{usuario_id}", response_model=Usuario)
def leer_usuario_por_id(usuario_id: int, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=Usuario)
def crear_usuario_endpoint(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario(db, usuario)

@router.put("/{usuario_id}", response_model=Usuario)
def actualizar_usuario_endpoint(usuario_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_actualizado = actualizar_usuario(db, usuario_id, usuario)
    if not usuario_actualizado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_actualizado

@router.delete("/{usuario_id}", response_model=Usuario)
def eliminar_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    usuario_eliminado = eliminar_usuario(db, usuario_id)
    if not usuario_eliminado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_eliminado