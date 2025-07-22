from fastapi import APIRouter, HTTPException
from app.core.database import get_connection

router = APIRouter()

# http://localhost:8000/api/obitos_causa/paraiba/2005/J189
@router.get("/obitos_causa/{estado}/{ano}/{causa}")
def contar_obitos_por_estado_ano_causa(estado: str, ano: str, causa: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        table_name = f"data_{estado.lower()}"
        query = f"""
            SELECT COUNT(*) FROM {table_name}
            WHERE "ANO_ARQUIVO"::INTEGER = %s
              AND "CAUSABAS" = %s
        """

        cursor.execute(query, (ano, causa))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()

        return {
            "estado": estado,
            "ano": ano,
            "causa": causa,
            "total_obitos": resultado[0]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
