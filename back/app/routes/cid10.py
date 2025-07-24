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
        ORDER BY id;
    """
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()

    categorias = {}
    categoria_atual = None

    for cid10, cat, subcat, descr in rows:
        if cat == 'S':  # É uma categoria
            categoria_atual = cid10
            categorias[categoria_atual] = {
                "descricao": descr,
                "subcategorias": []
            }
        elif subcat == 'S' and categoria_atual:
            categorias[categoria_atual]["subcategorias"].append({
                "cid10": cid10,
                "descricao": descr
            })

    result = [
        {
            "categoria": cat,
            "descricao": dados["descricao"],
            "subcategorias": dados["subcategorias"]
        }
        for cat, dados in categorias.items()
    ]
    return {"categorias": result}

