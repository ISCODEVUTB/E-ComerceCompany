import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.models import Usuario
from backend.app.logic.schemas import UsuarioCreate
from backend.app.crud import usuarios

def test_crear_usuario():
    db: Session = SessionLocal()
    usuario_data = UsuarioCreate(
        nombre="Test User",
        correo_electronico="test@example.com",
        rol="cliente",
        contrasena="123456"
    )
    usuario = usuarios.crear_usuario(db, usuario_data)
    assert usuario.nombre == "Test User"
    db.delete(usuario)
    db.commit()
    db.close()
