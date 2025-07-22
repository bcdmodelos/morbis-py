from fastapi import APIRouter, HTTPException
from app.core.database import get_connection

router = APIRouter()

@router.get("/obitos/{estado}/{ano}")
def contar_obitos_por_estado_ano(estado: str, ano: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Nome da tabela dinâmico
        table_name = f"data_{estado.lower()}"

        # Query para contar óbitos pelo ano
        query = f"""
            SELECT COUNT(*) FROM {table_name}
            WHERE "ANO_ARQUIVO"::INTEGER = %s
        """
        cursor.execute(query, (ano,))

        cursor.execute(query, (ano,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        return {"estado": estado, "ano": ano, "total_obitos": resultado[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))