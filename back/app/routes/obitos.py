from fastapi import APIRouter, HTTPException
from app.core.database import get_connection

router = APIRouter()

@router.get("/obitos/{estado}")
def contar_obitos(estado: str):
    tabela = f"data_{estado.lower()}"
    
    # Conexão com o banco
    conn = get_connection()
    cur = conn.cursor()

    try:
        # Verificar se a tabela existe
        cur.execute("""
            SELECT to_regclass(%s);
        """, (tabela,))
        existe = cur.fetchone()[0]

        if not existe:
            raise HTTPException(status_code=404, detail=f"Tabela para estado '{estado}' não encontrada.")

        # Contar registros
        cur.execute(f"SELECT COUNT(*) FROM {tabela};")
        total = cur.fetchone()[0]

        return {"estado": estado, "total_obitos": total}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()
