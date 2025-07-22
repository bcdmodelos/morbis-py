from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter()

@router.get("/estados")
def listar_estados():
    return {"message": "Lista de estados (em breve com dados do banco)"}
