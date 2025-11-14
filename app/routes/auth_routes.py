# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.config.mysql import SessionLocal
# from app.security.hashing import hash_password, verify_password
# from app.security.auth import crear_token
# from app.domain.user import UsuarioCreate, UsuarioLogin, UsuarioOut
# from app.models.usuario import Usuario

# router = APIRouter(prefix="/auth", tags=["Autenticación"])

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/register")
# def register(user: UsuarioCreate, db: Session = Depends(get_db)):
#     user_db = Usuario(
#         username=user.username,
#         email=user.email,
#         password_hash=hash_password(user.password)
#     )
#     db.add(user_db)
#     db.commit()
#     db.refresh(user_db)
#     return {"message": "Usuario creado"}

# @router.post("/login")
# def login(user: UsuarioLogin, db: Session = Depends(get_db)):
#     user_db = db.query(Usuario).filter(Usuario.username == user.username).first()
#     if not user_db or not verify_password(user.password, user_db.password_hash):
#         raise HTTPException(status_code=400, detail="Credenciales inválidas")
#     token = crear_token({"sub": user_db.username, "user_id": user_db.id})
#     return {"access_token": token, "token_type": "bearer"}
