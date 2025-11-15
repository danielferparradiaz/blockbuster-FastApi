from fastapi import APIRouter, Depends, HTTPException, status
from neo4j import Session
from app.config.neo4j import get_session
from app.cruds import crudAfiliado as crud
from app.domain.schemas.schemas import AfiliadoCreate, AfiliadoUpdate
from typing import List, Dict, Any

router = APIRouter(prefix="/afiliados", tags=["Afiliados (Neo4j)"])

@router.post("/", response_model=Dict[str, Any], status_code=status.HTTP_201_CREATED)
def crear_afiliado_route(afiliado: AfiliadoCreate, session: Session = Depends(get_session)):
    try:
        nuevo_afiliado = crud.crear_afiliado(session, afiliado)
        return nuevo_afiliado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear afiliado: {e}")

@router.get("/", response_model=List[Dict[str, Any]])
def obtener_afiliados_route(session: Session = Depends(get_session)):
    return crud.obtener_afiliados(session)

@router.get("/{id_afiliado}", response_model=Dict[str, Any])
def obtener_afiliado_route(id_afiliado: int, session: Session = Depends(get_session)):
    afiliado = crud.obtener_afiliado_por_id(session, id_afiliado)
    if afiliado is None:
        raise HTTPException(status_code=404, detail=f"Afiliado con ID {id_afiliado} no encontrado")
    return afiliado

@router.put("/{id_afiliado}", response_model=Dict[str, Any])
def actualizar_afiliado_route(id_afiliado: int, datos: AfiliadoUpdate, session: Session = Depends(get_session)):
    afiliado_actualizado = crud.actualizar_afiliado(session, id_afiliado, datos)
    if afiliado_actualizado is None:
        raise HTTPException(status_code=404, detail=f"Afiliado con ID {id_afiliado} no encontrado")
    return afiliado_actualizado

@router.delete("/{id_afiliado}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_afiliado_route(id_afiliado: int, session: Session = Depends(get_session)):
    if not crud.eliminar_afiliado(session, id_afiliado):
        raise HTTPException(status_code=404, detail=f"Afiliado con ID {id_afiliado} no encontrado")
    return