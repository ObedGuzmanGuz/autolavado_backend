from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    nombre: str
    estado: bool

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class RolResponse(RolBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
