import pytest

def test_register_and_authenticate(auth_module, sample_users):
    assert auth_module.register_user("alice", sample_users['alice']) is True
    assert auth_module.register_user("bob", sample_users['bob']) is True
    assert auth_module.register_user("alice", "otra") is False
    assert auth_module.authenticate("alice", sample_users['alice']) is True
    assert auth_module.authenticate("bob", sample_users['bob']) is True
    assert auth_module.authenticate("charlie","x") is False

def test_register_invalid_values(auth_module):
    with pytest.raises(ValueError):
        auth_module.register_user("", "pass")
    with pytest.raises(ValueError):
        auth_module.register_user("user", "")
@pytest.mark.parametrize("username,password", [
    ("user1","a"),
    ("user2", "long_password_!@#"),
    ("user3", 123456),
])

def test_parametrized_registration_and_auth(auth_module, username, password):
    assert auth_module.register_user(username, password) is True
    assert auth_module.authenticate(username, password) is True

def test_password_store_hashed(auth_module):
    auth_module.register_user("alice", "mypassword")
    raw = auth_module.get_hashed_password("alice")
    assert raw is not None
    assert "mypassword" not in raw
    assert len(raw)==64

def test_monkeypatch_hash_failure(auth_module, monkeypatch):
    def bad_hash(pw):
        raise RuntimeError("hash Error")
    monkeypatch.setattr(auth_module, "_hash_password", bad_hash)
    with pytest.raises(RuntimeError):
        auth_module.register_user("x", "y")
