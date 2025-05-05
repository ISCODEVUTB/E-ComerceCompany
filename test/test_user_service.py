
import pytest
from backend.user_service.service import UserService, User
from backend.user_service.app     import app, srv

@pytest.fixture
def us():
    return UserService()

@pytest.fixture
def sample_user():
    return User(id=1, name="Alice", email="alice@example.com", role="client")

def test_create_and_get_user(us, sample_user):
    us.create(sample_user)
    assert us.get(1) == sample_user

def test_update_user(us, sample_user):
    us.create(sample_user)
    updated = User(id=1, name="Alice Smith", email="alice@example.com", role="client")
    assert us.update(1, updated)
    assert us.get(1).name == "Alice Smith"

def test_delete_user(us, sample_user):
    us.create(sample_user)
    assert us.delete(1)
    assert us.get(1) is None


@pytest.fixture(autouse=True)
def clear_users():
    srv._users.clear()
    yield
    srv._users.clear()

@pytest.fixture
def client():
    app.testing = True
    app.config['WTF_CSRF_ENABLED'] = False
    return app.test_client()

def test_integration_create_and_list(client):
    payload = {"id": 2, "name": "Bob", "email": "bob@example.com", "role": "admin"}
    r1 = client.post("/users", json=payload)
    assert r1.status_code == 201

    r2 = client.get("/users")
    assert r2.status_code == 200
    data = r2.get_json()
    assert any(u["name"] == "Bob" for u in data)

def test_integration_get_user(client):
    client.post("/users", json={"id": 3, "name": "Carol", "email": "carol@example.com", "role": "client"})
    r = client.get("/users/3")
    assert r.status_code == 200
    assert r.get_json()["email"] == "carol@example.com"

def test_integration_not_found(client):
    r = client.get("/users/999")
    assert r.status_code == 404
