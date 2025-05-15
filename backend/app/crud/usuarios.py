from sqlalchemy.orm import Session
from ..models import Usuario
from ..schemas import UsuarioCreate

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def crear_usuario(db: Session, usuario: UsuarioCreate):
    nuevo_usuario = Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def actualizar_usuario(db: Session, usuario_id: int, usuario: UsuarioCreate):
    usuario_existente = obtener_usuario_por_id(db, usuario_id)
    if usuario_existente:
        for key, value in usuario.dict().items():
            setattr(usuario_existente, key, value)
        db.commit()
        db.refresh(usuario_existente)
    return usuario_existente

def eliminar_usuario(db: Session, usuario_id: int):
    usuario = obtener_usuario_por_id(db, usuario_id)
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario