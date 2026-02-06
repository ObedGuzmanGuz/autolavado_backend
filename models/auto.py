from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Auto(Base):
    __tablename__ = "c_auto"

    au_id = Column(Integer, primary_key=True, index=True)
    au_modelo = Column(String(45))
    au_matricula = Column(String(45))
    au_color = Column(String(45))
    au_tipo = Column(String(45))

    cl_id = Column(Integer, ForeignKey("c_cliente.cl_id"))

    cliente = relationship("Cliente", back_populates="autos")
    servicios = relationship("AutoServicio", back_populates="auto")
