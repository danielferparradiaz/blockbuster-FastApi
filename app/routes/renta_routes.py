from fastapi import APIRouter, Depends
from app.config.neo4j import get_session
from app.cruds import crudRenta as crud

router = APIRouter(prefix="/renta", tags=["Rentas (Neo4j)"])

@router.post("/")
def crear_renta(id_afiliado: int, id_titulo: int, session = Depends(get_session)):
    renta_id = crud.crear_renta(session, id_afiliado, id_titulo)
    return {"message": "Renta creada en Neo4j", "id_renta": renta_id}



@router.get("/historial")
def historial_rentas(session = Depends(get_session)):
    return crud.obtener_historial_rentas(session)

@router.get("/estadisticas")
def estadisticas_rentas(session = Depends(get_session)):
    return crud.obtener_estadisticas_rentas(session)
