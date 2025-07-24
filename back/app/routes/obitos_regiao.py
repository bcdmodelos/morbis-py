from fastapi import APIRouter, HTTPException
from app.core.database import get_connection
from app.core.regioes import REGIOES
from app.core.regioes import ESTADOS_NOMES

router = APIRouter()

# Exemplo: http://localhost:8000/api/obitos_regiao/nordeste/2005
@router.get("/obitos_regiao/{regiao}/{ano}")
def obitos_por_regiao(regiao: str, ano: str):
    try:
        regiao = regiao.lower()
        if regiao not in REGIOES:
            raise HTTPException(status_code=400, detail="Região inválida")

        estados = REGIOES[regiao]
        conn = get_connection()
        cur = conn.cursor()

        total_regiao = 0
        detalhes_estados = []

        for tabela in estados:
            query = f"""
                SELECT COUNT(*) FROM {tabela}
                WHERE "ANO_ARQUIVO" = %s
            """
            cur.execute(query, (ano,))
            result = cur.fetchone()
            count = result[0] if result else 0
            total_regiao += count
            nome_estado = ESTADOS_NOMES.get(tabela, tabela)
            detalhes_estados.append({"estado": nome_estado, "total_obitos": count})

        cur.close()
        conn.close()

        return {
            "regiao": regiao.capitalize(),
            "ano": ano,
            "total_obitos_regiao": total_regiao,
            "detalhes_estados": detalhes_estados
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))