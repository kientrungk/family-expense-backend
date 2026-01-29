from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET = "CHANGE_ME"
ALGO = "HS256"

pwd = CryptContext(schemes=["bcrypt"])

def hash_password(pw: str) -> str:
    return pwd.hash(pw)

def verify_password(pw: str, hashed: str) -> bool:
    return pwd.verify(pw, hashed)

def create_token(user_id: str):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGO)
