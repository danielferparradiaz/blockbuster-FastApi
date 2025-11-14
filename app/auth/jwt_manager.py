from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
import jwt

SECRET_KEY = "REALSECRETBABY"  # cámbialo por uno real
ALGORITHM = "HS256"

security = HTTPBearer()

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def validate_token(token: str) -> dict:
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return data
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

def auth_required(credentials = Depends(security)):
    token = credentials.credentials
    return validate_token(token)
