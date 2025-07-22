from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter()

# Endpoint exemplo
@router.get("/municipios")
def listar_municipios():
    return {"message": "Lista de municípios (em breve com dados do banco)"}
