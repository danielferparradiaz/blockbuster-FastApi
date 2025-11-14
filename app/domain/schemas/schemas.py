from pydantic import BaseModel
from typing import Optional
from datetime import date

class VisualizacionBase(BaseModel):
    id_afiliado: int
    id_titulo: int
    id_copia: int

class VisualizacionCreate(VisualizacionBase):
    pass

class VisualizacionResponse(VisualizacionBase):
    id_visualizacion: int
    fecha_inicio: date
    fecha_fin: date | None
    estado: str

    class Config:
        orm_mode = True

class AfiliadoCreate(BaseModel):
    IdAfiliado: int
    Nombres: str
    Apellidos: str
    Direccion: str
    Telefono: str
    FechaVinculacion: date
    Sexo: str
    FechaNacimiento: date
    NivelMembresia: str
    EstadoMembresia: str
    FechaInicioMembresia: date
    FechaFinMembresia: date

class AfiliadoUpdate(BaseModel):
    Nombres: Optional[str] = None
    Apellidos: Optional[str] = None
    Direccion: Optional[str] = None
    Telefono: Optional[str] = None
    NivelMembresia: Optional[str] = None
    EstadoMembresia: Optional[str] = None
    
# --- Título ---
class TituloCreate(BaseModel):
    IdTitulo: int
    Titulo: str
    Rating: str
    Anio: int
    Director: str
    DuracionMin: int

class TituloUpdate(BaseModel):
    Titulo: Optional[str] = None
    Rating: Optional[str] = None
    Anio: Optional[int] = None
    Director: Optional[str] = None
    DuracionMin: Optional[int] = None