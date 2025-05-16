import pytest
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from schemas import UsuarioCreate
import crud

def test_crear_usuario():
    db: Session = SessionLocal()
    usuario_data = UsuarioCreate(
        nombre="Test User",
        correo_electronico="test@example.com",
        rol="cliente",
        contrasena="123456"
    )
    usuario = crud.crear_usuario(db, usuario_data)
    assert usuario.nombre == "Test User"
    db.delete(usuario)
    db.commit()
    db.close()
