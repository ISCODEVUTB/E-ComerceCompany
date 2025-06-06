import pytest
from sqlalchemy.orm import Session
from backend.app.logic.database import SessionLocal
from backend.app.logic.schemas import DevolucionBase, UsuarioCreate, OrdenBase, CarritoBase
from backend.app.crud import devolutions, user, order, cart

def test_crear_devolucion():
    db: Session = SessionLocal()
    from backend.app.logic.models import Orden, Carrito, Usuario
    db.query(Orden).delete()
    db.query(Carrito).delete()
    db.query(Usuario).delete()
    db.commit()
    # 1. Crear usuario
    usuario_data = UsuarioCreate(
        nombre_usuario="Test User",
        correo_electronico="test@example.com",
        rol="cliente",
        contrasena="123456"
    )
    usuario = user.crear_usuario(db, usuario_data)
    # 2. Crear carrito
    carrito_data = CarritoBase(
        usuario_id=usuario.id,
        estado="abierto"
    )
    carrito = cart.crear_carrito(db, carrito_data)
    # 3. Crear orden
    orden_data = OrdenBase(
        usuario_id=usuario.id,
        carrito_id=carrito.id,
        monto_total=100.0,
        estado="pendiente"
    )
    orden = order.crear_orden(db, orden_data)
    # 4. Crear devolución
    devolucion_data = DevolucionBase(
        orden_id=orden.id,
        usuario_id=usuario.id,
        motivo="Producto defectuoso",
        estado="pendiente"
    )
    devolucion = devolutions.crear_devolucion(db, devolucion_data)
    assert devolucion.estado == "pendiente"
    assert devolucion.motivo == "Producto defectuoso"
    # 5. Limpiar registros
    db.delete(devolucion)
    db.delete(orden)
    db.delete(carrito)
    db.delete(usuario)
    db.commit()
    db.close()