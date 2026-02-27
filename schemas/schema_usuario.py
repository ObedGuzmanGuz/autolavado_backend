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
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    numero_telefono: Optional[str] = None
    estado: Optional[bool] = None


class UsuarioResponse(BaseModel):
    Id: int
    nombre: str
    correo_electronico: str
    fecha_registro: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {
        "from_attributes": True
    }