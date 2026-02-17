from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.rol import Rol
from schemas.schema_rol import RolCreate, RolResponse
from datetime import datetime
from typing import List

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RolResponse)
def crear_rol(rol: RolCreate, db: Session = Depends(get_db)):
    nuevo = Rol(
        **rol.dict(),
        fecha_registro=datetime.now(),
        fecha_actualizacion=datetime.now()
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=List[RolResponse])
def obtener_roles(db: Session = Depends(get_db)):
    return db.query(Rol).all()
