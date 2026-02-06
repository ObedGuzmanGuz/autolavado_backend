from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Servicio(Base):
    __tablename__ = "c_servicio"

    se_id = Column(Integer, primary_key=True, index=True)
    se_nombre = Column(String(80))
    se_descripcion = Column(String(850))
    se_precio = Column(DECIMAL(18,2))
    se_estatus = Column(String(45))

    us_id = Column(Integer, ForeignKey("c_usuario.us_id"))

    usuario = relationship("Usuario", back_populates="servicios")
    autos = relationship("AutoServicio", back_populates="servicio")
