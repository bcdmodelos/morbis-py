from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter()

# http://localhost:8000/api/municipios
@router.get("/municipios")
def listar_municipios():
    return {"message": "Lista de municípios (em breve com dados do banco)"}
