import os
import psycopg2
import pandas as pd

# ✅ Pega variáveis do ambiente (injetadas pelo Docker)
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "db")  # Nome do serviço no docker-compose
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

# ✅ Caminho para o arquivo CSV
CSV_PATH = "/app/data/cid/CID10.csv"

# ✅ Conecta ao banco
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# ✅ Cria tabela cid_10
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS cid_10 (
        id SERIAL PRIMARY KEY,
        cid10 VARCHAR(10),
        opc VARCHAR(10),
        cat VARCHAR(10),
        subcat VARCHAR(10),
        descr TEXT,
        restrsexo INT
    );
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Tabela 'cid_10' criada com sucesso!")

# ✅ Insere dados do CSV
def insert_data():
    df = pd.read_csv(CSV_PATH, delimiter=",", dtype=str).fillna("")  # Força string
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO cid_10 (cid10, opc, cat, subcat, descr, restrsexo)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, (row["CID10"], row["OPC"], row["CAT"], row["SUBCAT"], row["DESCR"], int(row["RESTRSEXO"]) if row["RESTRSEXO"].isdigit() else None))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Dados inseridos com sucesso!")

if __name__ == "__main__":
    create_table()
    insert_data()
