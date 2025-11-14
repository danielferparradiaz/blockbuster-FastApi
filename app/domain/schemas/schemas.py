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
