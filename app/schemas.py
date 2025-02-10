from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

#CLASE USUARIO
class Usuario(BaseModel):
    """
    Definir el modelo de datos para la entidad Usuario.

    Atributos:
        id (int): Identificador único del usuario.
        nombre (str): Nombre del usuario.
        correo (EmailStr): Correo electrónico del usuario (debe ser único).
        fecha_registro (datetime): Fecha y hora en que el usuario se registró.
    """
    nombre: str
    correo: EmailStr #propio de Pydantic para validar que sea un correo válido
    fecha_registro: datetime = datetime.now() #fecha actual por defecto
    id_proyecto: int

#CLASES PARA MODIFICAR UN USUARIO-> las creo para que no sean campos requeridos, que se puedan modificar si se quiere únicamnete
class UpdateUsuario(BaseModel):
    nombre: str = None
    correo: EmailStr = None
    id_proyecto: int = None


#CLASE PROYECTO
class Proyecto(BaseModel):
    nombre: str
    descripcion: Optional[str]
    fecha_inicio: date
    fecha_fin: date


#CLASE PARA MODIFICAR UN PROYECTO
class UpdateProyecto(BaseModel):
    fecha_inicio: date = None
    fecha_fin: date = None