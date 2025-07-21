import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv(dotenv_path="./back/.env")

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

# Diretório base
BASE_DIR = "./data/data_datasus"

# Mapeamento DATASUS -> nome tabela
mapa_estados = {
    "DOAC": "acre",
    "DOAL": "alagoas",
    "DOAP": "amapa",
    "DOAM": "amazonas",
    "DOBA": "bahia",
    "DOCE": "ceara",
    "DODF": "distrito_federal",
    "DOES": "espirito_santo",
    "DOGO": "goias",
    "DOMA": "maranhao",
    "DOMT": "mato_grosso",
    "DOMS": "mato_grosso_do_sul",
    "DOMG": "minas_gerais",
    "DOPA": "para",
    "DOPB": "paraiba",
    "DOPR": "parana",
    "DOPE": "pernambuco",
    "DOPI": "piaui",
    "DORJ": "rio_de_janeiro",
    "DORN": "rio_grande_do_norte",
    "DORS": "rio_grande_do_sul",
    "DORO": "rondonia",
    "DORR": "roraima",
    "DOSC": "santa_catarina",
    "DOSP": "sao_paulo",
    "DOSE": "sergipe",
    "DOTO": "tocantins"
}

# Conexão com o banco
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)
conn.autocommit = True
cur = conn.cursor()

for pasta, estado in mapa_estados.items():
    pasta_path = os.path.join(BASE_DIR, pasta)
    arquivo_csv = os.path.join(pasta_path, f"{pasta}_unificado.csv")
    
    if os.path.exists(arquivo_csv):
        tabela = f"data_{estado}"
        print(f"[INFO] Importando {arquivo_csv} para {tabela}...")

        try:
            with open(arquivo_csv, 'r', encoding='utf-8') as f:
                next(f)  # pular cabeçalho (opcional)
                cur.copy_expert(f"COPY {tabela} FROM STDIN WITH CSV DELIMITER ',' QUOTE '\"'", f)
            print(f"[✓] Dados carregados em {tabela}")
        except Exception as e:
            print(f"[ERRO] Falha ao importar {arquivo_csv}: {e}")
    else:
        print(f"[AVISO] Arquivo não encontrado: {arquivo_csv}")

cur.close()
conn.close()
print("[✓] Importação concluída!")