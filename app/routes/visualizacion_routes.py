from fastapi import APIRouter, Depends, HTTPException
from app.config.neo4j import get_session # ASUME que tienes esta función
from app.cruds import crudVisualizacion as crud  # Renombrado a crudVisualizacion
# from app.auth.oauth2 import get_current_user
from app.auth.jwt_manager import auth_required

# --- Definición del Router ---
# Cambiamos el prefijo y el tag de "renta" a "visualizacion"
router = APIRouter(prefix="/visualizacion", tags=["Visualizaciones (Neo4j)"])

# ----------------------------------------------------
# 🎬 Endpoints CRUD
# ----------------------------------------------------

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
        # Captura errores de validación (Afiliado/Título no encontrado)
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        # Captura errores de la base de datos
        raise HTTPException(status_code=500, detail="Error al crear la visualización: " + str(e))


@router.get("/historial")
def historial_visualizaciones(session = Depends(get_session)):
    # Usamos la nueva función renombrada
    return crud.obtener_historial_visualizaciones(session)

@router.get("/estadisticas")
def estadisticas_visualizaciones(session = Depends(get_session)):
    # Usamos la nueva función renombrada
    return crud.obtener_estadisticas_visualizaciones(session)

# NOTA: Se ha eliminado la función get_db ya que no se usa MySQL/SQLAlchemy
# NOTA: Se ha eliminado la lógica de actualización de estado de 'CopiaTitulo'