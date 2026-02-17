from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UsuarioBase(BaseModel):
    rol_Id: int
    nombre: str
    apellidoPaterno: str
    apellidoMaterno: str
    direccion: str
    correo_electronico: str
    numero_telefono: str
    estado: bool

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    direccion: Optional[str]
    numero_telefono: Optional[str]
    estado: Optional[bool]

class UsuarioResponse(UsuarioBase):
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True
