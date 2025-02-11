from fastapi import FastAPI
import uvicorn

from app.db.database import Base, engine
from app.routers import proyecto, tarea, usuario

def create_tables():
    Base.metadata.create_all(bind=engine)


#create_tables() -> solo llamar a este método una vez porque sino cada vez que se llame se crea de 0 la base de datos haciendo que los datos no sean persistentes

app = FastAPI()

app.include_router(proyecto.router)
app.include_router(usuario.router)
app.include_router(tarea.router)


#Ejecutar FastAPI
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)