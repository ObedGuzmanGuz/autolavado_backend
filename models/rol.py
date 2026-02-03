'''Esta clase permite generar el modelo para los tipos de rol'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime,Enum, Date
from sqlalchemy.orm import relationship
from config.db import Base


class Rol(Base):
    ''' Creacion de la tabla de roles en Mysql'''
    _tablemname_= "tbc_roles"
    Id = Column(Integer, primary_Key= True, index=True)
    nombreRol= Column(String(15))
    estado= Column(Boolean)
    


