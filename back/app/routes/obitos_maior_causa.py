from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter()

# http://localhost:8000/api/obitos_maior_causa/paraiba/2005
@router.get("/obitos_maior_causa/{estado}/{ano}")
async def maior_causa(estado: str, ano: str):
    try:
        conn = get_connection()
        cur = conn.cursor()

        tabela = f"data_{estado}"
        query = f"""
            SELECT "CAUSABAS", COUNT(*) as total
            FROM {tabela}
            WHERE "ANO_ARQUIVO" = %s
            GROUP BY "CAUSABAS"
            ORDER BY total DESC
            LIMIT 1;
        """

        cur.execute(query, (ano,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            return {
                "estado": estado,
                "ano": ano,
                "causa_mais_frequente": result[0],
                "total_obitos": result[1]
            }
        else:
            return {"message": "Nenhum dado encontrado para os filtros informados"}
    except Exception as e:
        return {"error": str(e)}
    