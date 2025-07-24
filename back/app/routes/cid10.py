from fastapi import APIRouter
from app.core.database import get_connection

router = APIRouter()

@router.get("/cid10")
def get_cid10():
    conn = get_connection()
    cur = conn.cursor()

    query = """
        SELECT cid10, cat, subcat, descr
        FROM cid_10
        ORDER BY cid10;
    """
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    categorias = {}
    for cid10, cat, subcat, descr in rows:
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append({
            "cid10": cid10,
            "subcat": subcat,
            "descricao": descr
        })

    result = [{"categoria": cat, "itens": itens} for cat, itens in categorias.items()]
    return {"categorias": result}
