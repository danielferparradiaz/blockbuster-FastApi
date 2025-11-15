# app/auth/dependencies.py
from fastapi import Depends
from fastapi.security import HTTPBearer
from .jwt_manager import decode_token

security = HTTPBearer()


def get_current_user(credentials = Depends(security)):
    token = credentials.credentials
    data = decode_token(token)
    return data   # retorna información completa del usuario
