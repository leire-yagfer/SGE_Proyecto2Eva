from sqlalchemy.orm import relationship
from sqlalchemy import Column, Date,Integer,String,Boolean,DateTime, Text
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from app.db.database import Base

#Modelo de la tabla usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now,onupdate=datetime.now)
    id_proyecto = Column(Integer, ForeignKey("proyectos.id"), nullable=False)

#Modelo de la tabla proyectos
class Proyecto(Base):
    __tablename__ = "proyectos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=True)

    #poner el id del proyecto en las tablas de usuario y tareas
    usuarios = relationship("Usuario", backref="usuario") #no pongo cascade porque si elimino el proyecto no elimino usuarios
    tareas = relationship("Tarea", backref="tarea", cascade="delete, merge")

#Modelo de la tabla tareas
class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    estado = Column(String(50), nullable=False)
    fecha_limite = Column(Date, nullable=True)
    proyecto_id = Column(Integer, ForeignKey("proyectos.id"), nullable=False)