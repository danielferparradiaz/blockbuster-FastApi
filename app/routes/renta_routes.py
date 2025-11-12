from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.config.mysql import SessionLocal
from app.domain import models        
from app.cruds import crudRenta as crud  

router = APIRouter(prefix="/renta", tags=["Rentas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def crear_renta(id_afiliado: int, id_copia: int, id_titulo: int, db: Session = Depends(get_db)):
    nueva_renta = models.Renta(
        id_afiliado=id_afiliado,
        id_copia=id_copia,
        id_titulo=id_titulo,
        fecha_renta=date.today(),
        fecha_devolucion=date.today() + timedelta(days=2),
        valor_renta=5000.00,
        valor_recargo=None
    )
    db.add(nueva_renta)

    # Actualizar estado de la copia
    copia = db.query(models.CopiaTitulo).filter_by(id_copia=id_copia, id_titulo=id_titulo).first()
    if copia:
        copia.estado = models.EstadoEnum.RENTADA

    db.commit()
    db.refresh(nueva_renta)
    return {"message": "Renta creada", "renta": nueva_renta.id_renta}


#  Endpoint 1: Historial de rentas
@router.get("/historial")
def historial_rentas(db: Session = Depends(get_db)):
    return crud.obtener_historial_rentas(db)


#  Endpoint 2: Estadísticas de rentas
@router.get("/estadisticas")
def estadisticas_rentas(db: Session = Depends(get_db)):
    return crud.obtener_estadisticas_rentas(db)
