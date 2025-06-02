import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.models import Usuario
from backend.app.logic.schemas import UsuarioCreate
from backend.app.crud import user

def test_crear_usuario():
    db: Session = SessionLocal()
    from backend.app.logic.models import Usuario
    db.query(Usuario).delete()
    db.commit()
    usuario_data = UsuarioCreate(
        nombre_usuario="Test User",
        correo_electronico="test@example.com",
        rol="cliente",
        contraseña="123456"
    )
    usuario = user.crear_usuario(db, usuario_data)
    assert usuario.nombre_usuario == "Test User"
    db.delete(usuario)
    db.commit()
    db.close()
