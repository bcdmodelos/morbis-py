from fastapi import APIRouter, Response
from app.core.database import get_connection
import pandas as pd
import io

router = APIRouter()

@router.get("/download/cid10")
def download_cid10():
    conn = get_connection()
    query = """
        SELECT cid10, cat, subcat, descr
        FROM cid_10
        ORDER BY id;
    """
    df = pd.read_sql(query, conn)
    conn.close()

    # Converter para CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, sep=';', encoding='utf-8')
    csv_buffer.seek(0)

    headers = {
        'Content-Disposition': 'attachment; filename="cid10_dados.csv"',
        'Content-Type': 'text/csv',
    }

    return Response(content=csv_buffer.getvalue(), media_type="text/csv", headers=headers)
