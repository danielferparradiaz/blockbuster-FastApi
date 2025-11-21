# app/main.py

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.routes import visualizacion_routes, afiliado_routes, titulo_routes
from app.auth.jwt_manager import create_token


app = FastAPI(
    title="🎬 Blockbuster API",
    version="2.0",
    description="Implementación del modelo Blockbuster usando Neo4j",
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    schema = get_openapi(
        title=app.title, version=app.version,
        description=app.description, routes=app.routes
    )

    schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", [{"HTTPBearer": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# @app.post("/login")
# def login(credentials: dict):
#     email = credentials["email"]
#     password = credentials["password"]

#     # 1. Buscar usuario en BD
#     user = get_user_by_email(email)

#     if not user or user.password != password:
#         raise HTTPException(status_code=401, detail="Credenciales incorrectas")

#     # 2. Verificar que el usuario tenga membresía
#     if not user.FechaInicioMembresia or not user.FechaFinMembresia:
#         raise HTTPException(
#             status_code=403,
#             detail="El usuario no tiene membresía configurada"
#         )

#     # 3. Crear token usando jwt_manager
#     token = create_token(
#         user_id=user.IdAfiliado,
#         role=user.rol,
#         membership_start=str(user.FechaInicioMembresia),
#         membership_end=str(user.FechaFinMembresia)
#     )

#     return {
#         "access_token": token,
#         "token_type": "bearer"
#     }    



@app.post("/login")
def login():
    token = create_token(
        user_id=1,
        role="usuario",
        membership_start="2024-01-01",
        membership_end="2025-01-01"
    )
    return {"token": token}


app.include_router(visualizacion_routes.router)
app.include_router(afiliado_routes.router)
app.include_router(titulo_routes.router)

