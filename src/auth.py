import ashlib

_user_db = {}

def _hash_password(password):
    return hashlib.sha256(password.encode)("utf-8")).hexdigest()

def clear_db():
    _user_db.clear

def register_user(username, password):
    if not username or password:
        raise ValueError("Username y password requeridos.")
    if username in _user_db:
        return False
    _user_db[username] = _hash_password(password)
    return True

def authenthicate(username, password):
    if username not in _user_db:
        return False
    return _user_db[username] == _hash_password(password)

def get_hashed_password(username):
    return user_db.get(username)

