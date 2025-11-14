from fastapi import FastAPI
from app.config.mysql import engine, Base
from app.domain.models import models
from app.routes import renta_routes, auth_routes

app = FastAPI(
    title="🎬 Blockbuster Graph API",
    version="2.0 (Neo4j Edition)",
    description="Implementación del modelo Blockbuster usando base de datos de grafos Neo4j"
)

app.include_router(renta_routes.router)
# app.include_router(renta_routes.router)

@app.get("/")
def root():
    return {"message": "🌐 Bienvenido a Blockbuster Graph API con Neo4j"}
