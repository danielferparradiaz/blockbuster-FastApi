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

    schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = schema
    return schema


app.openapi = custom_openapi


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
