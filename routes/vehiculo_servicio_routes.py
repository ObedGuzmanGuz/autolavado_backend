from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.model_vehiculo_servicio_usuario import VehiculoServicioUsuario
from schemas.schema_vehiculo_servicio import (
    VehiculoServicioCreate,
    VehiculoServicioResponse
)
from datetime import datetime
from typing import List

router = APIRouter(prefix="/vehiculo-servicios", tags=["Vehiculo Servicios"])

@router.post("/", response_model=VehiculoServicioResponse)
def crear_asignacion(data: VehiculoServicioCreate, db: Session = Depends(get_db)):
    nueva = vehiculoServicio(
        **data.dict(),
        fecha_registro=datetime.now(),
        fecha_actualizacion=datetime.now()
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.get("/", response_model=List[VehiculoServicioResponse])
def obtener_asignaciones(db: Session = Depends(get_db)):
    return db.query(vehiculoServicio).all()

@router.get("/{id}", response_model=VehiculoServicioResponse)
def obtener_asignacion(id: int, db: Session = Depends(get_db)):
    asignacion = db.query(vehiculoServicio).filter(vehiculoServicio.Id == id).first()
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return asignacion

@router.delete("/{id}")
def eliminar_asignacion(id: int, db: Session = Depends(get_db)):
    asignacion = db.query(vehiculoServicio).filter(vehiculoServicio.Id == id).first()
    if not asignacion:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")

    db.delete(asignacion)
    db.commit()
    return {"mensaje": "Asignación eliminada correctamente"}
