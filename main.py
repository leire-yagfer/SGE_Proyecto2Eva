from fastapi import FastAPI
import uvicorn

from app.db.database import Base, engine
from app.routers import proyecto, usuario

def create_tables():
    Base.metadata.create_all(bind=engine)


#create_tables()

app = FastAPI()

app.include_router(usuario.router)
app.include_router(proyecto.router)


#Ejecutar FastAPI
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)