from fastapi import APIRouter, Depends

from app.db import models
from app.db.database import get_db
from app.schemas import UpdateUsuario, Usuario

from sqlalchemy.orm import Session

listausuarios = []

router = APIRouter(
 prefix="/usuario",
 tags=["Usuarios"]
)

#OBTENER TODOS LOS USUARIOS
@router.get("/obtener_usuarios")
def obtener_usuarios(db:Session=Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    print (usuarios)
    return listausuarios


#OBTENER USUARIO POR ID -> ÚTIL PARA VER A QUÉ PROYECTO PERTENECE
@router.get("/obtener_usuario_por_id/{user_id}")
def obtener_usuario_por_id(user_id:int,db:Session=Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == user_id).first() #obtengo el usuario cuyo id es el pasado por parámetro
    if not usuario:
        return{"Respuesta": "Usuario no encontrado"}
    return usuario


#CREAR UN NUEVO USUARIO
@router.post("/crear_usuario")
def crear_usuario(user:Usuario, db:Session=Depends(get_db)):
    newUser = user.model_dump()
    nuevo_usuario = models.Usuario(
        #no añado ni el id ni la fecha de registro porque el id es autoincrementable y la fecha se obtiene de la que sea actualmente
        nombre = newUser["nombre"],
        correo = newUser["correo"],
        id_proyecto = newUser["id_proyecto"]
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    listausuarios.append(newUser)
    return{"Respuesta": "Usuario creado"}


#ELIMINAR UN USUARIO POR SU ID
@router.delete("/elimar_usuario/{user_id}")
def eliminar_usuario_por_id(user_id:int, db:Session=Depends(get_db)):
    deleteUser = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if not deleteUser:
        return {"Respuesta": "Usuario no encontrado"}
    db.delete(deleteUser)
    db.commit
    return {"Respuesta": "Usuario eliminado correctamente"}


#MODIFICAR USUARIOS
@router.patch("/modificar_usuario/{user_id}")
def actualizar_usuario_por_id(user_id:int, updateUser:UpdateUsuario, db:Session=Depends(get_db)):
    actualizarUser = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if not actualizarUser:
        return {"Respuesta": "Usuario no encontrado"}
    actualizarUser.update(updateUser.model_dump(exclude_unset=True)) #parámetro que indica que sólo se actualicen los campos que están llegando, no todos.
    db.commit
    return { "Respuesta": "Usuario actualizado correctamente"}