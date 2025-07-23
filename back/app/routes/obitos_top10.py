from fastapi import APIRouter, HTTPException
from app.core.database import get_connection

router = APIRouter()

# http://localhost:8000/api/obitos_top10/paraiba/2005
@router.get("/obitos_top10/{estado}/{ano}")
def obitos_top10(estado: str, ano: str):
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Nome da tabela baseado no estado
        tabela = f"data_{estado.lower()}"

        # 1. Total geral de óbitos no ano
        query_total = f"""
            SELECT COUNT(*) FROM {tabela}
            WHERE "ANO_ARQUIVO" = %s
        """
        cur.execute(query_total, (ano,))
        total_ano = cur.fetchone()[0]

        # 2. Top 10 causas de óbitos
        query_top10 = f"""
            SELECT "CAUSABAS", COUNT(*) as total
            FROM {tabela}
            WHERE "ANO_ARQUIVO" = %s
            GROUP BY "CAUSABAS"
            ORDER BY total DESC
            LIMIT 10
        """
        cur.execute(query_top10, (ano,))
        top10_result = cur.fetchall()

        # Calcula total das 10 mais
        total_top10 = sum(row[1] for row in top10_result)

        cur.close()
        conn.close()

        # Monta resposta
        top10_causas = [{"causa": row[0], "quantidade": row[1]} for row in top10_result]

        return {
            "estado": estado,
            "ano": ano,
            "total_obitos_ano": total_ano,
            "total_obitos_top10": total_top10,
            "top10_causas": top10_causas
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))