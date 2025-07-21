import os
import psycopg2
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv(dotenv_path="./back/.env")

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")

# Lista dos estados
estados = [
    "acre", "alagoas", "amapa", "amazonas", "bahia", "ceara", "distrito_federal",
    "espirito_santo", "goias", "maranhao", "mato_grosso", "mato_grosso_do_sul",
    "minas_gerais", "para", "paraiba", "parana", "pernambuco", "piaui",
    "rio_de_janeiro", "rio_grande_do_norte", "rio_grande_do_sul", "rondonia",
    "roraima", "santa_catarina", "sao_paulo", "sergipe", "tocantins"
]

# Colunas fornecidas
colunas = [
    "ACIDTRAB","ALTCAUSA","ASSISTMED","ATESTADO","ATESTANTE","CAUSABAS","CAUSABAS_O",
    "CAUSAMAT","CB_PRE","CIRCOBITO","CIRURGIA","CODBAIOCOR","CODBAIRES","CODCART","CODESTAB",
    "CODIFICADO","CODMUNCART","CODMUNNATU","CODMUNOCOR","CODMUNRES","COMUNSVOIM","CONTADOR",
    "CRM","DIFDATA","DTATESTADO","DTCADASTRO","DTCADINF","DTCADINV","DTCONCASO","DTCONINV",
    "DTINVESTIG","DTNASC","DTOBITO","DTRECEBIM","DTRECORIG","DTRECORIGA","DTREGCART","ESC",
    "ESC2010","ESCFALAGR1","ESCMAE","ESCMAE2010","ESCMAEAGR1","ESTABDESCR","ESTCIV","EXAME",
    "EXPDIFDATA","FONTE","FONTEINV","FONTES","FONTESINF","GESTACAO","GRAVIDEZ","HORAOBITO",
    "IDADE","IDADEMAE","LINHAA","LINHAB","LINHAC","LINHAD","LINHAII","LOCOCOR","MORTEPARTO",
    "NATURAL","NECROPSIA","NUDIASINF","NUDIASOBCO","NUDIASOBIN","NUMERODN","NUMEROLOTE",
    "NUMREGCART","OBITOGRAV","OBITOPARTO","OBITOPUERP","OCUP","OCUPMAE","ORIGEM","PARTO",
    "PESO","QTDFILMORT","QTDFILVIVO","RACACOR","SEMAGESTAC","SERIESCFAL","SERIESCMAE","SEXO",
    "STCODIFICA","STDOEPIDEM","STDONOVA","TIPOBITO","TPASSINA","TPMORTEOCO","TPNIVELINV",
    "TPOBITOCOR","TPPOS","TPRESGINFO","UFINFORM","Unnamed: 0","VERSAOSCB","VERSAOSIST",
    "contador","ANO_ARQUIVO"
]

# Conexão
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)
conn.autocommit = True
cur = conn.cursor()

for estado in estados:
    tabela = f"data_{estado}"
    print(f"[INFO] Criando tabela {tabela}...")
    cur.execute(f"DROP TABLE IF EXISTS {tabela};")

    colunas_sql = ', '.join([f'"{col}" TEXT' for col in colunas])
    create_table_sql = f"CREATE TABLE {tabela} ({colunas_sql});"
    cur.execute(create_table_sql)

print("[✓] Todas as tabelas foram criadas com sucesso!")
cur.close()
conn.close()