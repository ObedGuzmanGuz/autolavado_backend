'''Esta clase permite generar el modelo para los tipos de user'''
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.db import Base


class User(Base):
     '''Clase para especificar tabla usuarios'''
     _tablemname_= "tbb_usuarios"
      Id = Column(Integer, primary_Key= True, index=True)
      Rol_Id= Column(Integer, ForeignKey("tbc_roles.Id"))
      Nombre= Column(String(60))
      primerApellido= Column(String(60))
      Correo_Electronico=Column(String(100))
      




