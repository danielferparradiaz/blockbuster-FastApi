from fastapi import APIRouter, Depends, HTTPException
from app.config.neo4j import get_session
from app.cruds import crudVisualizacion as crud
from app.auth.jwt_manager import auth_required


router = APIRouter(prefix="/visualizacion", tags=["Visualizaciones (Neo4j)"])

@router.post("/")
def crear_visualizacion(
    id_afiliado: int,
    id_titulo: int,
    session = Depends(get_session),
    user = Depends(auth_required)
):
    try:
        resultado = crud.crear_visualizacion(session, id_afiliado, id_titulo, user)
        
        return {
            "message": "Visualización creada exitosamente",
            "id_visualizacion": resultado["id_visualizacion"]
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail="Error al crear la visualización: " + str(e))


@router.get("/historial")
def historial_visualizaciones(session = Depends(get_session)):
    return crud.obtener_historial_visualizaciones(session)

@router.get("/estadisticas")
def estadisticas_visualizaciones(session = Depends(get_session)):
    return crud.obtener_estadisticas_visualizaciones(session)