from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.auto import Auto
from schemas.schema_auto import AutoCreate, AutoResponse
from datetime import datetime
from typing import List

router = APIRouter(prefix="/autos", tags=["Autos"])

@router.post("/", response_model=AutoResponse)
def crear_auto(auto: AutoCreate, db: Session = Depends(get_db)):
    nuevo_auto = Auto(
        **auto.dict(),
        fecha_registro=datetime.now(),
        fecha_actualizacion=datetime.now()
    )
    db.add(nuevo_auto)
    db.commit()
    db.refresh(nuevo_auto)
    return nuevo_auto
 
@router.get("/", response_model=List[AutoResponse])
def obtener_autos(db: Session = Depends(get_db)):
    return db.query(Auto).all()

@router.get("/{auto_id}", response_model=AutoResponse)
def obtener_auto(auto_id: int, db: Session = Depends(get_db)):
    auto = db.query(Auto).filter(Auto.Id == auto_id).first()
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto
