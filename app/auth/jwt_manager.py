# app/auth/jwt_manager.py
from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer

SECRET_KEY = "SUPER_SECRET_KEY_CHANGE_THIS"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24
security = HTTPBearer()


def create_token(user_id: int, role: str, membership_start: str, membership_end: str):
    payload = {
        "sub": str(user_id),
        "role": role,
        "membership_start": membership_start,
        "membership_end": membership_end,
        "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="❌ Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="❌ Token inválido")


def auth_required(credentials = Depends(security)):
    token = credentials.credentials
    return decode_token(token)
