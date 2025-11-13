from fastapi import FastAPI
from app.config.mysql import engine, Base
from app.domain.models import models
from app.routes import renta_routes


app = FastAPI(
    title="🎬 Blockbuster Graph API",
    version="1.0 (MYSQL Edition)",
    description="Implementación del modelo Blockbuster usando base de datos MySQL"
)

app.include_router(renta_routes.router)

# Crear las tablas automáticamente
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "🎬 Bienvenido a la API Blockbuster"}
