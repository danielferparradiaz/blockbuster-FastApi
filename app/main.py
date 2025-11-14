from fastapi import FastAPI
from app.routes import visualizacion_routes, afiliado_routes, titulo_routes

app = FastAPI(
    title="🎬 Blockbuster Graph API",
    version="2.0 (Neo4j Edition)",
    description="Implementación del modelo Blockbuster usando base de datos de grafos Neo4j"
)

@app.post("/login")
def login():
    token = create_token({"user_id": 1, "role": "admin"})
    return {"token": token}

app.include_router(visualizacion_routes.router)
app.include_router(afiliado_routes.router)
app.include_router(titulo_routes.router)