from fastapi import FastAPI
from app.routes import estados, municipios

app = FastAPI(title="MORBIS API")

app.include_router(estados.router, prefix="/api")
app.include_router(municipios.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend funcionando!"}