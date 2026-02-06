'''Esta clase permite generar el modelo para los tipos de user'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Usuario(Base):
    __tablename__ = "c_usuario"

    us_id = Column(Integer, primary_key=True, index=True)
    us_nombre = Column(String(60))
    us_apellidoPaterno = Column(String(60))
    us_apellidoMaterno = Column(String(60))
    us_usuario = Column(String(60), unique=True)
    us_password = Column(String(256))

    ro_id = Column(Integer, ForeignKey("c_rol.ro_id"))

    rol = relationship("Rol", back_populates="usuarios")
    servicios = relationship("Servicio", back_populates="usuario")
