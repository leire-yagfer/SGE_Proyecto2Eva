from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

#CLASE USUARIO
class Usuario(BaseModel):
    nombre: str
    correo: EmailStr #propio de Pydantic para validar que sea un correo válido
    fecha_registro: datetime = datetime.now() #fecha actual por defecto
    id_proyecto: int

#CLASE PROYECTO
class Proyecto(BaseModel):
    nombre: str
    descripcion: Optional[str]
    fecha_inicio: date
    fecha_fin: date

#CLASE TAREA
class Tarea(BaseModel):
    nombre: str
    descripcion: Optional[str]
    estado: str
    fecha_limite: date
    proyecto_id: int


#Clases para modificar registros de la base de datos -> la creo para que no sean campos requeridos, que se puedan modificar si se quiere únicamnete
#CLASE PARA MODIFICAR UN USUARIO 
class UpdateUsuario(BaseModel):
    nombre: str = None
    correo: EmailStr = None
    id_proyecto: int = None

#CLASE PARA MODIFICAR UN PROYECTO 
class UpdateProyecto(BaseModel):
    fecha_inicio: date = None
    fecha_fin: date = None

#CLASE PARA MODIFICAR UNA TAREA
class UpdateTarea(BaseModel):
    estado: str = None
    fecha_limite: date = None