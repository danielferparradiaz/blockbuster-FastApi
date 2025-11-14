from fastapi import FastAPI
from app.routes import renta_routes

app = FastAPI(
    title="🎬 Blockbuster Graph API",
    version="2.0 (Neo4j Edition)",
    description="Implementación del modelo Blockbuster usando base de datos de grafos Neo4j"
)

@app.post("/login")
def login():
    token = create_token({"user_id": 1, "role": "admin"})
    return {"token": token}

app.include_router(renta_routes.router)

@app.get("/")
def root():
    return {"message": "🌐 Bienvenido a Blockbuster Graph API con Neo4j"}
