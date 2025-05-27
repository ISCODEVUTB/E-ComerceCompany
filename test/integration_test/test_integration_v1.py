import pytest
from fastapi.testclient import TestClient
from backend.app.logic.main import app
from backend.app.logic.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use SQLite for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_main.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hola Mundo"}

# --- USUARIOS ---
def test_crud_usuarios():
    # Create
    usuario = {
        "nombre": "Juan",
        "correo_electronico": "juan@test.com",
        "rol": "cliente",
        "contrasena": "1234"
    }
    r = client.post("/usuarios/", json=usuario)
    assert r.status_code == 200
    data = r.json()
    usuario_id = data["id"]
    assert data["nombre"] == usuario["nombre"]

    # List
    r = client.get("/usuarios/")
    assert r.status_code == 200
    assert any(u["id"] == usuario_id for u in r.json())

    # Get by id
    r = client.get(f"/usuarios/{usuario_id}")
    assert r.status_code == 200
    assert r.json()["id"] == usuario_id

    # Update
    update = usuario.copy()
    update["nombre"] = "Juan Actualizado"
    r = client.put(f"/usuarios/{usuario_id}", json=update)
    assert r.status_code == 200
    assert r.json()["nombre"] == "Juan Actualizado"

    # Delete
    r = client.delete(f"/usuarios/{usuario_id}")
    assert r.status_code == 200
    assert r.json()["id"] == usuario_id

    # Not found after delete
    r = client.get(f"/usuarios/{usuario_id}")
    assert r.status_code == 404

# --- PRODUCTOS ---
def test_crud_productos():
    producto = {
        "nombre": "Producto Test",
        "descripcion": "Desc",
        "precio": 10.5,
        "inventario": 100
    }
    r = client.post("/productos/", json=producto)
    assert r.status_code == 200
    data = r.json()
    producto_id = data["id"]
    assert data["nombre"] == producto["nombre"]

    r = client.get("/productos/")
    assert r.status_code == 200
    assert any(p["id"] == producto_id for p in r.json())

    r = client.get(f"/productos/{producto_id}")
    assert r.status_code == 200
    assert r.json()["id"] == producto_id

    update = producto.copy()
    update["nombre"] = "Producto Actualizado"
    r = client.put(f"/productos/{producto_id}", json=update)
    assert r.status_code == 200
    assert r.json()["nombre"] == "Producto Actualizado"

    r = client.delete(f"/productos/{producto_id}")
    assert r.status_code == 200
    assert r.json()["id"] == producto_id

    r = client.get(f"/productos/{producto_id}")
    assert r.status_code == 404

# --- CARRITOS ---
def test_crud_carritos():
    # Primero, crear un usuario
    usuario = {
        "nombre": "CarritoUser",
        "correo_electronico": "carrito@test.com",
        "rol": "cliente",
        "contrasena": "1234"
    }
    r = client.post("/usuarios/", json=usuario)
    usuario_id = r.json()["id"]

    carrito = {
        "usuario_id": usuario_id,
        "estado": "activo"
    }
    r = client.post("/carritos/", json=carrito)
    assert r.status_code == 200
    data = r.json()
    carrito_id = data["id"]
    assert data["usuario_id"] == usuario_id

    r = client.get("/carritos/")
    assert r.status_code == 200
    assert any(c["id"] == carrito_id for c in r.json())

    r = client.get(f"/carritos/{carrito_id}")
    assert r.status_code == 200
    assert r.json()["id"] == carrito_id

    update = carrito.copy()
    update["estado"] = "cerrado"
    r = client.put(f"/carritos/{carrito_id}", json=update)
    assert r.status_code == 200
    assert r.json()["estado"] == "cerrado"

    r = client.delete(f"/carritos/{carrito_id}")
    assert r.status_code == 200
    assert r.json()["id"] == carrito_id

    r = client.get(f"/carritos/{carrito_id}")
    assert r.status_code == 404

# --- ORDENES ---
def test_crud_ordenes():
    # Crear usuario y carrito primero
    usuario = {
        "nombre": "OrdenUser",
        "correo_electronico": "orden@test.com",
        "rol": "cliente",
        "contrasena": "1234"
    }
    r = client.post("/usuarios/", json=usuario)
    usuario_id = r.json()["id"]

    carrito = {
        "usuario_id": usuario_id,
        "estado": "activo"
    }
    r = client.post("/carritos/", json=carrito)
    carrito_id = r.json()["id"]

    orden = {
        "usuario_id": usuario_id,
        "carrito_id": carrito_id,
        "monto_total": 99.99,
        "estado": "pendiente"
    }
    r = client.post("/ordenes/", json=orden)
    assert r.status_code == 200
    data = r.json()
    orden_id = data["id"]
    assert data["usuario_id"] == usuario_id

    r = client.get("/ordenes/")
    assert r.status_code == 200
    assert any(o["id"] == orden_id for o in r.json())

    r = client.get(f"/ordenes/{orden_id}")
    assert r.status_code == 200
    assert r.json()["id"] == orden_id

    update = orden.copy()
    update["estado"] = "completada"
    r = client.put(f"/ordenes/{orden_id}", json=update)
    assert r.status_code == 200
    assert r.json()["estado"] == "completada"

    r = client.delete(f"/ordenes/{orden_id}")
    assert r.status_code == 200
    assert r.json()["id"] == orden_id

    r = client.get(f"/ordenes/{orden_id}")
    assert r.status_code == 404

# --- DEVOLUCIONES ---
def test_crud_devoluciones():
    # Crear usuario, carrito y orden primero
    usuario = {
        "nombre": "DevolUser",
        "correo_electronico": "devol@test.com",
        "rol": "cliente",
        "contrasena": "1234"
    }
    r = client.post("/usuarios/", json=usuario)
    usuario_id = r.json()["id"]

    carrito = {
        "usuario_id": usuario_id,
        "estado": "activo"
    }
    r = client.post("/carritos/", json=carrito)
    carrito_id = r.json()["id"]

    orden = {
        "usuario_id": usuario_id,
        "carrito_id": carrito_id,
        "monto_total": 50.0,
        "estado": "pendiente"
    }
    r = client.post("/ordenes/", json=orden)
    orden_id = r.json()["id"]

    devolucion = {
        "orden_id": orden_id,
        "usuario_id": usuario_id,
        "motivo": "No me gustó"
    }
    r = client.post("/devoluciones/", json=devolucion)
    assert r.status_code == 200
    data = r.json()
    devolucion_id = data["id"]
    assert data["orden_id"] == orden_id

    r = client.get("/devoluciones/")
    assert r.status_code == 200
    assert any(d["id"] == devolucion_id for d in r.json())

    r = client.get(f"/devoluciones/{devolucion_id}")
    assert r.status_code == 200
    assert r.json()["id"] == devolucion_id

    update = devolucion.copy()
    update["motivo"] = "Producto defectuoso"
    r = client.put(f"/devoluciones/{devolucion_id}", json=update)
    assert r.status_code == 200
    assert r.json()["motivo"] == "Producto defectuoso"

    r = client.delete(f"/devoluciones/{devolucion_id}")
    assert r.status_code == 200
    assert r.json()["id"] == devolucion_id

    r = client.get(f"/devoluciones/{devolucion_id}")
    assert r.status_code == 404