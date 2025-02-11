from fastapi import APIRouter, Depends

from app.db import models
from app.db.database import get_db
from app.schemas import Proyecto, UpdateProyecto

from sqlalchemy.orm import Session

listaproyectos = []

router = APIRouter(
 prefix="/proyecto",
 tags=["Proyectos"]
)

#OBTENER TODOS LOS PROYECTOS
@router.get("/obtener_proyectos")
def obtener_proyectos(db:Session=Depends(get_db)):
    proyectos = db.query(models.ProyectoTable).all()
    print (proyectos)
    return listaproyectos


#OBTENER PROYECTO POR ID -> ÚTIL PARA VER LA INFO DE UN PROYECTO EN CONCRETO
@router.post("/obtener_proyecto_por_id/{proyecto_id}")
def obtener_proyecto_por_id(proyecto_id:int,db:Session=Depends(get_db)):
    proyecto = db.query(models.ProyectoTable).filter(models.ProyectoTable.id == proyecto_id).first() #obtengo el proyecto cuyo id es el pasado por parámetro
    if proyecto:
        print(proyecto.nombre)
        return proyecto
    return{"Respuesta": "Proyecto no encontrado"}
    


#CREAR UN NUEVO PROYECTO
@router.post("/crear_proyecto")
def crear_proyecto(proyecto:Proyecto, db:Session=Depends(get_db)):
    newProject = proyecto.model_dump()
    nuevo_proyecto = models.ProyectoTable(
        #no añado ni el id ni la fecha de registro porque el id es autoincrementable y la fecha se obtiene de la que sea actualmente
        nombre = newProject["nombre"],
        descripcion = newProject["descripcion"],
        fecha_inicio = newProject["fecha_inicio"],
        fecha_fin = newProject["fecha_fin"],
    )
    db.add(nuevo_proyecto)
    db.commit()
    db.refresh(nuevo_proyecto)
    listaproyectos.append(newProject)
    return{"Respuesta": "Proyecto creado"}


#ELIMINAR UN PROYECTO POR SU ID
@router.delete("/elimar_proyecto/{proyecto_id}")
def eliminar_proyecto_por_id(proyecto_id:int, db:Session=Depends(get_db)):
    deleteProject = db.query(models.ProyectoTable).filter(models.ProyectoTable.id == proyecto_id).first()
    if not deleteProject:
        return {"Respuesta": "Proyecto no encontrado"}
    db.delete(deleteProject)
    db.commit
    return {"Respuesta": "Proyecto eliminado correctamente"}


#MODIFICAR PROYECTOS -> solo fecha de inicio y fin
@router.put("/modificar_proyecto/{proyecto_id}")
def actualizar_proyecto_por_id(proyecto_id:int, updateProject:UpdateProyecto, db:Session=Depends(get_db)):
    actualizarProject = db.query(models.ProyectoTable).filter(models.ProyectoTable.id == proyecto_id).first()
    if actualizarProject:
        actualizarProject.fecha_inicio = updateProject.fecha_inicio
        actualizarProject.fecha_fin = updateProject.fecha_fin
    db.commit
    db.commit(actualizarProject)
    return { "Respuesta": "Proyecto actualizado correctamente"}