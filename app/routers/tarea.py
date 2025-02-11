from fastapi import APIRouter, Depends

from app import schemas
from app.db import models
from app.db.database import get_db
from app.schemas import Tarea, UpdateTarea

from sqlalchemy.orm import Session

router = APIRouter(
 prefix="/tarea",
 tags=["Tareas"]
)

#OBTENER TODAS LAS TAREAS
@router.get("/obtener_tareas")
def obtener_tareas(db:Session=Depends(get_db)):
    tareas = db.query(models.TareaTable).all()
    print(tareas)
    return tareas


#OBTENER TAREAS POR ID -> ÚTIL PARA VER LA INFO DE UNA TAREA CONCRETA
@router.post("/obtener_tarea_por_id/{tarea_id}")
def obtener_tarea_por_id(tarea_id:int,db:Session=Depends(get_db)):
    tarea = db.query(models.TareaTable).filter(models.TareaTable.id == tarea_id).first() #obtengo la tarea cuyo id es el pasado por parámetro
    if tarea:
        print(tarea.nombre)
        return tarea
    return{"Respuesta": "Tarea no encontrado"}


#OBETNER TAREAS POR ID DEL PROYECTO (FK) -> ÚTIL PARA VER CUÁNTAS TAREAS HAY RELACIONADAS A UN PROYECTO Y EN QUÉ CNSISTE CADA UNA
@router.post("/obtener_tarea_por_id_proyecto/{proyecto_id}")
def obtener_tarea_por_id_proyecto(proyecto_id:int,db:Session=Depends(get_db)):
    proyecto_tarea = db.query(models.TareaTable).filter(models.TareaTable.proyecto_id == proyecto_id).all() #obtengo todas aquellas tareas que tienen el id_proyecto igual
    if proyecto_tarea:
        return proyecto_tarea
    return{"Respuesta": "Tareas pertenecientes al proyecto no encontradas"}


#CREAR UNA NUEVA TAREA
@router.post("/crear_tarea")
def crear_tarea(tarea:Tarea, db:Session=Depends(get_db)):
    newTask = tarea.model_dump()
    nueva_tarea = models.TareaTable(
        #no añado el id porque es autoincrementable
        nombre = newTask["nombre"],
        descripcion = newTask["descripcion"],
        estado = newTask["estado"],
        fecha_limite = newTask["fecha_limite"],
        proyecto_id = newTask["proyecto_id"],
    )
    db.add(nueva_tarea)
    db.commit()
    return{"Respuesta": "Tarea creada"}


#ELIMINAR UNA TAREA POR SU ID
@router.delete("/eliminar_tarea/{tarea_id}")
def elimar_tarea(tarea_id:int, db:Session=Depends(get_db)):
    deleteTask = db.query(models.TareaTable).filter(models.TareaTable.id == tarea_id).first()
    if not deleteTask:
        return {"Respuesta": "Tarea no encontrada"}
    db.delete(deleteTask)
    db.commit()
    return {"Respuesta": "Tarea eliminada correctamente"}


#MODIFICAR TAREAS -> solo fecha límite y el estado
@router.put("/modificar_tarea/{tarea_id}")
def actualizar_tarea_por_id(tarea_id:int, updateTask:UpdateTarea, db:Session=Depends(get_db)):
    actualizarTask = db.query(models.TareaTable).filter(models.TareaTable.id == tarea_id).first()
    if actualizarTask:
        actualizarTask.estado = updateTask.estado
        actualizarTask.fecha_limite = updateTask.fecha_limite
        db.commit()
        return { "Respuesta": "Tarea actualizada correctamente"}
    else:
        return {"Respuesta": "Tarea no encontrada"}