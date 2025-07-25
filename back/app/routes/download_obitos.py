from fastapi import APIRouter, Response, HTTPException
from app.core.database import get_connection
import pandas as pd
import io

router = APIRouter()

estados = [
    "acre", "alagoas", "amapa", "amazonas", "bahia", "ceara", "distrito_federal",
    "espirito_santo", "goias", "maranhao", "mato_grosso", "mato_grosso_do_sul",
    "minas_gerais", "para", "paraiba", "parana", "pernambuco", "piaui",
    "rio_de_janeiro", "rio_grande_do_norte", "rio_grande_do_sul", "rondonia",
    "roraima", "santa_catarina", "sao_paulo", "sergipe", "tocantins"
]

@router.get("/download_obitos/{estado}")
def download_obitos(estado: str):
    estado = estado.lower()
    if estado not in estados:
        raise HTTPException(status_code=400, detail="Estado inválido")

    table_name = f"data_{estado}"

    conn = get_connection()
    try:
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, conn)
    finally:
        conn.close()

    # Converter para CSV em memória
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, sep=';', encoding='utf-8')
    csv_buffer.seek(0)

    headers = {
        "Content-Disposition": f'attachment; filename="{table_name}.csv"',
        "Content-Type": "text/csv",
    }

    return Response(content=csv_buffer.getvalue(), media_type="text/csv", headers=headers)
