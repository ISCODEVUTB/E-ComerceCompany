import pytest
from fastapi.testclient import TestClient
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.logic.main import app
from backend.app.logic.database import Base, get_db  # Ajusta según tu estructura

# Crea una base de datos SQLite en memoria para pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea las tablas en la base de datos de prueba
Base.metadata.create_all(bind=engine)

# Dependency override para usar la base de datos de prueba
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_query_example():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_create_item():
    payload = {"name": "Test Item", "description": "A test item"}
    response = client.post("/items/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert "id" in data

def test_get_item_by_id():
    payload = {"name": "Another Item", "description": "Another test"}
    post_response = client.post("/items/", json=payload)
    item_id = post_response.json()["id"]
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == item_id
    assert data["name"] == "Another Item"

def test_update_item():
    # Crea un item
    payload = {"name": "Update Me", "description": "To be updated"}
    post_response = client.post("/items/", json=payload)
    item_id = post_response.json()["id"]
    # Actualiza el item
    update_payload = {"name": "Updated Item", "description": "Updated description"}
    put_response = client.put(f"/items/{item_id}", json=update_payload)
    assert put_response.status_code == 200
    data = put_response.json()
    assert data["name"] == "Updated Item"
    assert data["description"] == "Updated description"

def test_delete_item():
    # Crea un item
    payload = {"name": "Delete Me", "description": "To be deleted"}
    post_response = client.post("/items/", json=payload)
    item_id = post_response.json()["id"]
    # Elimina el item
    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 204
    # Verifica que ya no existe
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404

def test_create_item_missing_fields():
    # Intenta crear un item sin campos requeridos
    payload = {"description": "Missing name"}
    response = client.post("/items/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity

# Para ejecutar los tests usa el siguiente comando en la terminal:
# pytest app/tests/test_integracion.py