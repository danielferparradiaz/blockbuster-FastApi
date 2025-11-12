# from pydantic import BaseModel
# from datetime import date
# from typing import Optional

# class AfiliadoBase(BaseModel):
#     nombres: str
#     apellidos: str
#     direccion: Optional[str] = None
#     telefono: Optional[str] = None

# class AfiliadoCreate(AfiliadoBase):
#     fecha_vinculacion: date
#     sexo: str
#     fecha_nacimiento: date
#     id_principal: Optional[int] = None

# class Afiliado(AfiliadoBase):
#     id_afiliado: int

#     class Config:
#         orm_mode = True 
