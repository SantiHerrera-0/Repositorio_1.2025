import pytest
from src import auth

@pytest.fixture(autouse=True)
def clean_db():
    auth.clear_db()
    yield
    auth.clear_db()

@pytest.fixture
def auth_module():
    return auth

@pytest.fixture
def sample_users():
    return{
        "alice": "password123",
        "bob": "s3cret!",
}


