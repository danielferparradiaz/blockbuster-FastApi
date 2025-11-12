from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta

from app.domain.models import models
from app.domain import schemas


# CREATE
def crear_renta(db: Session, id_afiliado: int, id_copia: int, id_titulo: int):
    renta = models.Renta(
        id_afiliado=id_afiliado,
        id_copia=id_copia,
        id_titulo=id_titulo,
        fecha_renta=date.today(),
        fecha_devolucion=date.today() + timedelta(days=2),
        valor_renta=5000.00
    )
    db.add(renta)

    copia = db.query(models.CopiaTitulo).filter_by(
        id_copia=id_copia, id_titulo=id_titulo
    ).first()
    if copia:
        copia.estado = models.EstadoEnum.RENTADA

    db.commit()
    db.refresh(renta)
    return renta

# READ
def obtener_rentas(db: Session):
    return db.query(models.Renta).all()


# Consulta 1: Historia de rentas por afiliado
def obtener_historial_rentas(db: Session):
    query = db.query(
        func.upper(models.Afiliado.nombres).label("Nombres"),
        func.upper(models.Afiliado.apellidos).label("Apellidos"),
        func.concat(
            func.upper(func.left(models.Titulo.titulo, 1)),
            func.lower(func.substring(models.Titulo.titulo, 2))
        ).label("Titulo"),
        func.date_format(models.Renta.fecha_renta, "%d de %M de %Y").label("FechaRenta"),
        func.datediff(models.Renta.fecha_devolucion, models.Renta.fecha_renta).label("DuracionDias")
    ).join(models.Renta, models.Renta.id_afiliado == models.Afiliado.id_afiliado)\
     .join(models.Titulo, models.Renta.id_titulo == models.Titulo.id_titulo)

    return query.all()

# Consulta 2: Cantidad y totales de rentas por título
def obtener_estadisticas_rentas(db: Session):
    query = db.query(
        models.Titulo.titulo.label("Titulo"),
        func.count(models.Renta.id_renta).label("CantidadRentas"),
        func.sum(models.Renta.valor_renta).label("TotalRentas"),
        func.sum(func.coalesce(models.Renta.valor_recargo, 0)).label("TotalRecargos")
    ).join(models.Titulo, models.Renta.id_titulo == models.Titulo.id_titulo)\
     .group_by(models.Titulo.titulo)

    return query.all()