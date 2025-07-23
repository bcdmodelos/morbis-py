from fastapi import APIRouter, HTTPException
from app.core.database import get_connection

router = APIRouter()

# http://localhost:8000/api/obitos_bottom10/paraiba/2005
@router.get("/obitos_bottom10/{estado}/{ano}")
def obitos_bottom10(estado: str, ano: str):
    try:
        conn = get_connection()
        cur = conn.cursor()

        tabela = f"data_{estado.lower()}"

        # Total geral de óbitos no ano
        query_total = f"""
            SELECT COUNT(*) FROM {tabela}
            WHERE "ANO_ARQUIVO" = %s
        """
        cur.execute(query_total, (ano,))
        total_ano = cur.fetchone()[0]

        # As 10 menos frequentes
        query_bottom10 = f"""
            SELECT "CAUSABAS", COUNT(*) as total
            FROM {tabela}
            WHERE "ANO_ARQUIVO" = %s
            GROUP BY "CAUSABAS"
            ORDER BY total ASC
            LIMIT 10
        """
        cur.execute(query_bottom10, (ano,))
        bottom10_result = cur.fetchall()

        # Soma dos menores
        total_bottom10 = sum(row[1] for row in bottom10_result)

        cur.close()
        conn.close()

        bottom10_causas = [{"causa": row[0], "quantidade": row[1]} for row in bottom10_result]

        return {
            "estado": estado,
            "ano": ano,
            "total_obitos_ano": total_ano,
            "total_obitos_bottom10": total_bottom10,
            "bottom10_causas": bottom10_causas
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
