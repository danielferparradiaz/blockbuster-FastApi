# ====================================================
# app/routes/titulo_routes.py
# Rutas de FastAPI para el CRUD de Titulo
# ====================================================

from fastapi import APIRouter, Depends, HTTPException, status
from neo4j import Session
from app.config.neo4j import get_session # ASUME que existe
from app.cruds import crudTitulo as crud
from app.domain.schemas.schemas import TituloCreate, TituloUpdate
from typing import List, Dict, Any

router = APIRouter(prefix="/titulos", tags=["Títulos (Neo4j)"])

# --- CREATE ---
@router.post("/", response_model=Dict[str, Any], status_code=status.HTTP_201_CREATED)
def crear_titulo_route(titulo: TituloCreate, session: Session = Depends(get_session)):
    try:
        nuevo_titulo = crud.crear_titulo(session, titulo)
        return nuevo_titulo
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear título: {e}")

# --- READ ALL ---
@router.get("/", response_model=List[Dict[str, Any]])
def obtener_titulos_route(session: Session = Depends(get_session)):
    return crud.obtener_titulos(session)

# --- READ BY ID ---
@router.get("/{id_titulo}", response_model=Dict[str, Any])
def obtener_titulo_route(id_titulo: int, session: Session = Depends(get_session)):
    titulo = crud.obtener_titulo_por_id(session, id_titulo)
    if titulo is None:
        raise HTTPException(status_code=404, detail=f"Título con ID {id_titulo} no encontrado")
    return titulo

# --- UPDATE ---
@router.put("/{id_titulo}", response_model=Dict[str, Any])
def actualizar_titulo_route(id_titulo: int, datos: TituloUpdate, session: Session = Depends(get_session)):
    titulo_actualizado = crud.actualizar_titulo(session, id_titulo, datos)
    if titulo_actualizado is None:
        raise HTTPException(status_code=404, detail=f"Título con ID {id_titulo} no encontrado")
    return titulo_actualizado

# --- DELETE ---
@router.delete("/{id_titulo}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_titulo_route(id_titulo: int, session: Session = Depends(get_session)):
    if not crud.eliminar_titulo(session, id_titulo):
        raise HTTPException(status_code=404, detail=f"Título con ID {id_titulo} no encontrado")
    return