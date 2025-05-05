import pytest
from backend.user_service.service import UserService, User

@ pytest.fixture
def us():
    return UserService()

@ pytest.fixture
def sample_user():
    return User(id=1, name="Alice", email="alice@example.com", role="client")

 def test_create_and_get_user(us, sample_user):
    us.create(sample_user)
    user = us.get(1)
    assert user == sample_user

 def test_update_user(us, sample_user):
    us.create(sample_user)
    updated = User(id=1, name="Alice Smith", email="alice@example.com", role="client")
    assert us.update(1, updated)
    assert us.get(1).name == "Alice Smith"

 def test_delete_user(us, sample_user):
    us.create(sample_user)
    assert us.delete(1)
    assert us.get(1) is None
