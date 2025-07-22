from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter()

# http://localhost:8000/api/estados
@router.get("/estados")
def listar_estados():
    return {"message": "Lista de estados (em breve com dados do banco)"}
