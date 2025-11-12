from sqlalchemy import (
    Column, Integer, String, Date, Enum, ForeignKey, ForeignKeyConstraint, DECIMAL
)
from sqlalchemy.orm import relationship
from app.config.mysql import engine, Base
import enum

# ==========================
# ENUMS
# ==========================
class SexoEnum(str, enum.Enum):
    M = "M"
    F = "F"

class EstadoEnum(str, enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    RENTADA = "RENTADA"
    DAÑADA = "DAÑADA"

class FormatoEnum(str, enum.Enum):
    DVD = "DVD"
    BLUERAY = "BLUERAY"
    VHS = "VHS"


# ==========================
# TABLA: AFILIADO
# ==========================
class Afiliado(Base):
    __tablename__ = "afiliado"

    id_afiliado = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(50), nullable=False)
    apellidos = Column(String(50), nullable=False)
    direccion = Column(String(100))
    telefono = Column(String(20))
    fecha_vinculacion = Column(Date, nullable=False)
    sexo = Column(Enum(SexoEnum))
    fecha_nacimiento = Column(Date)
    id_principal = Column(Integer, ForeignKey("afiliado.id_afiliado"), nullable=True)

    principal = relationship("Afiliado", remote_side=[id_afiliado])


# ==========================
# TABLA: TITULO
# ==========================
class Titulo(Base):
    __tablename__ = "titulo"

    id_titulo = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), unique=True, nullable=False)
    descripcion = Column(String(255))
    rating = Column(String(30))
    categoria = Column(String(50))
    fecha_liberacion = Column(Date)

    copias = relationship("CopiaTitulo", back_populates="titulo")


# ==========================
# TABLA: COPIA_TITULO
# ==========================
class CopiaTitulo(Base):
    __tablename__ = "copia_titulo"

    id_copia = Column(Integer, primary_key=True)
    id_titulo = Column(Integer, ForeignKey("titulo.id_titulo"), primary_key=True)
    estado = Column(Enum(EstadoEnum), default=EstadoEnum.DISPONIBLE)
    formato = Column(Enum(FormatoEnum), nullable=False)

    titulo = relationship("Titulo", back_populates="copias")
    rentas = relationship("Renta", back_populates="copia")


# ==========================
# TABLA: RENTA
# ==========================
class Renta(Base):
    __tablename__ = "renta"

    id_renta = Column(Integer, primary_key=True, autoincrement=True)
    id_afiliado = Column(Integer, ForeignKey("afiliado.id_afiliado"), nullable=False)
    id_copia = Column(Integer, nullable=False)
    id_titulo = Column(Integer, nullable=False)
    fecha_renta = Column(Date)
    fecha_devolucion = Column(Date)
    valor_renta = Column(DECIMAL(10, 2))
    valor_recargo = Column(DECIMAL(10, 2), nullable=True)

    # Clave foránea compuesta hacia copia_titulo
    __table_args__ = (
        ForeignKeyConstraint(
            ["id_copia", "id_titulo"],
            ["copia_titulo.id_copia", "copia_titulo.id_titulo"]
        ),
    )

    afiliado = relationship("Afiliado")
    copia = relationship("CopiaTitulo", back_populates="rentas")
